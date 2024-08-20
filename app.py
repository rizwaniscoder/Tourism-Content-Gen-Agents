import streamlit as st
import os
import re
import sys
import requests
from datetime import datetime
from dotenv import load_dotenv, set_key
from crewai import Crew, Process
from agents import MarketingAnalysisAgents
from tasks import MarketingAnalysisTasks
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

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

# Sidebar options for customization
st.sidebar.title("Customization Options")
target_audience = st.sidebar.selectbox("Target Audience", ["None", "Teens", "Adults", "Professionals"])
platform = st.sidebar.selectbox("Platform", ["None", "Instagram", "Facebook", "Twitter", "LinkedIn"])
tone_of_voice = st.sidebar.selectbox("Tone of Voice", ["None", "Formal", "Casual", "Humorous", "Inspirational"])
keywords = st.sidebar.text_input("Keywords (comma separated)")
image_style = st.sidebar.selectbox("Image Style", ["None", "Minimalist", "Vintage", "Modern", "Artistic"])

# Initialize OpenAI client
openai_client = ChatOpenAI(api_key=openai_api_key)

# Initialize tasks and agents
tasks = MarketingAnalysisTasks()
agents = MarketingAnalysisAgents()

def generate_content():
    expander = st.expander("Crew Log")
    sys.stdout = StreamToExpander(expander)

    try:
        # Create Agents
        product_competitor_agent = agents.product_competitor_agent()
        strategy_planner_agent = agents.strategy_planner_agent()
        creative_agent = agents.creative_content_creator_agent()
        senior_photographer = agents.senior_photographer_agent()
        chief_creative_director = agents.chief_creative_director_agent()

        # Initialize Tasks
        website_analysis = tasks.product_analysis(product_competitor_agent)
        market_analysis = tasks.competitor_analysis(product_competitor_agent)

        # Generate marketing campaign and ad copy if options are selected
        campaign_development = None
        write_copy = None
        if platform != "None" and tone_of_voice != "None" and target_audience != "None":
            campaign_development = tasks.campaign_development(strategy_planner_agent, platform=platform, tone=tone_of_voice, audience=target_audience)
            write_copy = tasks.instagram_ad_copy(creative_agent, keywords=keywords)

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
            ] if campaign_development and write_copy else [website_analysis, market_analysis]
        )

        ad_copy = copy_crew.kickoff() if campaign_development and write_copy else None

        # Create Tasks for Image
        image_description = None
        if image_style != "None" and ad_copy:
            take_photo = tasks.take_photograph_task(senior_photographer, ad_copy, style=image_style)
            approve_photo = tasks.review_photo(chief_creative_director)
            image_crew = Crew(
                agents=[
                    senior_photographer,
                    chief_creative_director
                ],
                tasks=[
                    take_photo,
                    approve_photo
                ]
            )
            image_description = image_crew.kickoff()

        # Generate and Display Image using DALL-E
        def generate_image(description):
            if description:
                prompt_template = PromptTemplate(
                    input_variables=["image_desc"],
                    template="Generate an image based on the following description: {image_desc}"
                )
                prompt = prompt_template.format(image_desc=description)
                chain = LLMChain(llm=openai_client, prompt=prompt_template)
                image_url = DallEAPIWrapper().run(chain.run(prompt))
                return image_url
            return None

        image_url = generate_image(image_description) if image_description else None

        # Display Results
        st.markdown("## Here is the result")
        if ad_copy:
            st.markdown("### Your post copy:")
            st.write(ad_copy)

        if image_url:
            st.markdown("### Your Generated Image:")
            st.image(image_url, caption="Generated Image", use_column_width=True)

        # Save results to a text file with utf-8 encoding
        filename = f"generated_content_{datetime.today().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            if ad_copy:
                f.write(f"Instagram Caption:\n{ad_copy}\n\n")
            if image_url:
                f.write(f"Generated Image URL: {image_url}\n")

        # Download link for the text file
        with open(filename, "rb") as f:
            st.download_button(
                label="Download Captions and Image Info",
                data=f,
                file_name=filename,
                mime="text/plain"
            )
    except Exception as e:
        st.error(f"An error occurred: {e}")
    finally:
        sys.stdout = sys.__stdout__

if st.button("Generate Marketing Strategy"):
    generate_content()
