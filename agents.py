import os
from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import logging

# Set up logging to handle any potential errors
logging.basicConfig(level=logging.ERROR)

class MarketingAnalysisAgents:
    def __init__(self):
        try:
            self.llm = ChatOpenAI(model_name="gpt-4o-mini")
            self.serper_dev_tool = SerperDevTool()
            self.scrape_website_tool = ScrapeWebsiteTool()
        except Exception as e:
            logging.error(f"Failed to initialize LLM or tools: {e}")
            raise

    def product_competitor_agent(self):
        try:
            return Agent(
                role="Lead Market Analyst",
                goal=dedent("""\
                    Conduct amazing analysis of the products and
                    competitors, providing in-depth insights to guide
                    marketing strategies."""),
                backstory=dedent("""\
                    As the Lead Market Analyst at a premier
                    digital marketing firm, you specialize in dissecting
                    online business landscapes."""),
                tools=[
                    self.serper_dev_tool,
                    self.scrape_website_tool
                ],
                allow_delegation=False,
                llm=self.llm,
                verbose=True
            )
        except Exception as e:
            logging.error(f"Failed to create Product Competitor Agent: {e}")
            raise

    def strategy_planner_agent(self):
        try:
            return Agent(
                role="Chief Marketing Strategist",
                goal=dedent("""\
                    Synthesize amazing insights from product analysis
                    to formulate incredible marketing strategies."""),
                backstory=dedent("""\
                    You are the Chief Marketing Strategist at
                    a leading digital marketing agency, known for crafting
                    bespoke strategies that drive success."""),
                tools=[
                    self.serper_dev_tool,
                    self.scrape_website_tool
                ],
                llm=self.llm,
                verbose=True
            )
        except Exception as e:
            logging.error(f"Failed to create Strategy Planner Agent: {e}")
            raise

    def creative_content_creator_agent(self):
        try:
            return Agent(
                role="Creative Content Creator",
                goal=dedent("""\
                    Develop compelling and innovative content
                    for social media campaigns, with a focus on creating
                    high-impact Instagram ad copies."""),
                backstory=dedent("""\
                    As a Creative Content Creator at a top-tier
                    digital marketing agency, you excel in crafting narratives
                    that resonate with audiences on social media.
                    Your expertise lies in turning marketing strategies
                    into engaging stories and visual content that capture
                    attention and inspire action."""),
                tools=[
                    self.serper_dev_tool,
                    self.scrape_website_tool
                ],
                llm=self.llm,
                verbose=True
            )
        except Exception as e:
            logging.error(f"Failed to create Creative Content Creator Agent: {e}")
            raise

    def senior_photographer_agent(self):
        try:
            return Agent(
                role="Senior Photographer",
                goal=dedent("""\
                    Take the most amazing photographs for Instagram ads that
                    capture emotions and convey a compelling message."""),
                backstory=dedent("""\
                    As a Senior Photographer at a leading digital marketing
                    agency, you are an expert at taking amazing photographs that
                    inspire and engage, you're now working on a new campaign for a super
                    important customer and you need to take the most amazing photograph."""),
                tools=[
                    self.serper_dev_tool,
                    self.scrape_website_tool
                ],
                llm=self.llm,
                allow_delegation=False,
                verbose=True
            )
        except Exception as e:
            logging.error(f"Failed to create Senior Photographer Agent: {e}")
            raise

    def chief_creative_director_agent(self):
        try:
            return Agent(
                role="Chief Creative Director",
                goal=dedent("""\
                    Oversee the work done by your team to make sure it's the best
                    possible and aligned with the product's goals, review, approve,
                    ask clarifying questions or delegate follow-up work if necessary to make
                    decisions"""),
                backstory=dedent("""\
                    You're the Chief Content Officer of a leading digital
                    marketing agency specializing in product branding. You're working on a new
                    customer, trying to make sure your team is crafting the best possible
                    content for the customer."""),
                tools=[
                    self.serper_dev_tool,
                    self.scrape_website_tool
                ],
                llm=self.llm,
                verbose=True
            )
        except Exception as e:
            logging.error(f"Failed to create Chief Creative Director Agent: {e}")
            raise