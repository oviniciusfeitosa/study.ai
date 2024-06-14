from crewai import Agent
# from langchain.llms import OpenAI
from tools import BrowserTool, CalculatorTool,SearchTool
# Test
import os
# from langchain_openai import ChatOpenAI

# from langchain_community.llms import Ollama
# ollama_model = Ollama(model=os.environ['OPENAI_MODEL_NAME'])
from langchain_community.tools import DuckDuckGoSearchRun

from langchain_community.chat_models import ChatOllama
ollama_model = ChatOllama(model=os.environ['OPENAI_MODEL_NAME'], base_url = "http://localhost:11434")
search_tool = DuckDuckGoSearchRun()
class TripAgents():

  def city_selection_agent(self):
    return Agent(
        # role='City Selection Expert',
        role='city selection expert',
        goal='Select the best city based on weather, season, and prices',
        backstory=
        'An expert in analyzing travel data to pick ideal destinations',
        tools=[
            # SearchTool.search_internet,
            search_tool,
            BrowserTool.scrape_and_summarize_website,
        ],
        verbose=True
        # ,allow_delegation=False
        # ,llm=ChatOpenAI(model_name=os.environ['OPENAI_MODEL_NAME'], temperature=0.7, base_url = "http://localhost:11434/v1")
        ,llm=ollama_model
        )

  def local_expert(self):
    return Agent(
        # role='Local Expert at this city',
        role='local expert at this city',
        goal='Provide the BEST insights about the selected city',
        backstory="""A knowledgeable local guide with extensive information
        about the city, it's attractions and customs""",
        tools=[
            # SearchTool.search_internet,
            search_tool,
            BrowserTool.scrape_and_summarize_website,
        ],
        verbose=True
        # ,allow_delegation=False
        # ,llm=ChatOpenAI(model_name=os.environ['OPENAI_MODEL_NAME'], temperature=0.7, base_url = "http://localhost:11434/v1"))
        ,llm=ollama_model)

  def travel_concierge(self):
    return Agent(
        # role='Amazing Travel Concierge',
        role='amazing travel concierge',
        goal="""Create the most amazing travel itineraries with budget and 
        packing suggestions for the city""",
        backstory="""Specialist in travel planning and logistics with 
        decades of experience""",
        tools=[
            # SearchTool.search_internet,
            search_tool,
            BrowserTool.scrape_and_summarize_website,
            CalculatorTool.calculate,
        ],
        verbose=True
        # ,allow_delegation=False
        # ,llm=ChatOpenAI(model_name=os.environ['OPENAI_MODEL_NAME'], temperature=0.7, base_url = "http://localhost:11434/v1")
        ,llm=ollama_model
                        )