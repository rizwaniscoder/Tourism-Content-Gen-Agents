import streamlit as st
import os
import re
import sys
import tempfile
from crewai import Crew, Process
from agents import MarketingAnalysisAgents
from tasks import MarketingAnalysisTasks
from dotenv import load_dotenv, set_key
from langchain_openai import ChatOpenAI
from datetime import datetime
import requests

# Load environment variables
load_dotenv()

class StreamToExpander:
    def __init__(self, expander, buffer_limit=10000):
        self.expander = expander
        self.buffer = []
        self.buffer_limit = buffer_limit

    def write(self, data):
        cleaned_data = re.sub(r'\x1B\[\d+;?\d*m', '', data)
        if len(self.buffer) >= self.buffer_limit:
            self.buffer.pop(0)
        self.buffer.append(cleaned_data)

        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer.clear()

    def flush(self):
        if self.buffer:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer.clear()

# Set page config
st.set_page_config(
    page_title='Australia Travel Safe Marketing Strategy',
    layout="centered"
)

st.title('Australia Travel Safe Marketing Strategy')
st.markdown("### Welcome to the marketing Crew")
st.markdown('-------------------------------')

# Get API keys from the user
st.sidebar.title("API Keys")
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
serper_api_key = st.sidebar.text_input("SERPER API Key", type="password")

if openai_api_key:
    os.environ["OPENAI_API_KEY"] = openai_api_key
    set_key('.env', 'OPENAI_API_KEY', openai_api_key)
if serper_api_key:
    os.environ["SERPER_API_KEY"] = serper_api_key
    set_key('.env', 'SERPER_API_KEY', serper_api_key)

# Initialize OpenAI client
openai_client = ChatOpenAI(api_key=openai_api_key)

# Initialize tasks and agents
tasks = MarketingAnalysisTasks()
agents = MarketingAnalysisAgents()

if st.button("Generate Marketing Strategy"):
    expander = st.expander("Crew Log")
    sys.stdout = StreamToExpander(expander)

    try:
        # Create Agents
        product_competitor_agent = agents.product_competitor_agent()
        strategy_planner_agent = agents.strategy_planner_agent()
        creative_agent = agents.creative_content_creator_agent()

        # Create Tasks
        website_analysis = tasks.product_analysis(product_competitor_agent)
        market_analysis = tasks.competitor_analysis(product_competitor_agent)
        campaign_development = tasks.campaign_development(strategy_planner_agent)
        write_copy = tasks.instagram_ad_copy(creative_agent)

        # Create Crew responsible for Copy
        copy_crew = Crew(
            agents=[
                product_competitor_agent,
                strategy_planner_agent,
                creative_agent
            ],
            tasks=[
                website_analysis,
                market_analysis,
                campaign_development,
                write_copy
            ],
            verbose=True
        )

        ad_copy = copy_crew.kickoff()

        # Create Crew responsible for Image
        senior_photographer = agents.senior_photographer_agent()
        chief_creative_diretor = agents.chief_creative_diretor_agent()

        # Create Tasks for Image
        take_photo = tasks.take_photograph_task(senior_photographer, ad_copy)
        approve_photo = tasks.review_photo(chief_creative_diretor)

        image_crew = Crew(
            agents=[
                senior_photographer,
                chief_creative_diretor
            ],
            tasks=[
                take_photo,
                approve_photo
            ],
            verbose=True
        )

        image = image_crew.kickoff()

        # Display Results
        st.markdown("## Here is the result")
        st.markdown("### Your post copy:")
        st.write(ad_copy)

        st.markdown("### Your DALL-E 3 description:")
        st.write(image)

        # Generate and Display Image using OpenAI DALL-E 3
        def generate_image(prompt):
            response = openai_client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1
            )
            image_url = response.data[0].url

            # Download image
            image_data = requests.get(image_url).content
            image_filename = f"generated_image_{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            with open(image_filename, "wb") as img_file:
                img_file.write(image_data)

            return image_filename, image_url

        image_filename, image_url = generate_image(image)
        st.image(image_url, caption="Generated Image", use_column_width=True)

        # Save results to a text file
        filename = f"generated_content_{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Generated Image URL: {image_url}\n\n")
            f.write(f"Instagram Caption:\n{ad_copy}\n\n")

        # Download link for the text file
        with open(filename, "rb") as f:
            st.download_button(
                label="Download Captions",
                data=f,
                file_name=filename,
                mime="text/plain"
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        sys.stdout = sys.__stdout__
