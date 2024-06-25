import os
from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_community.chat_models import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from trip_planner_crew.tools.browser_tools import BrowserTool
from trip_planner_crew.tools.calculator_tool import CalculatorTool
from crewai_tools import WebsiteSearchTool
#from trip_planner_crew.tools.searh_tool import SearchTool
# from langchain_groq import ChatGroq
# from langchain.llms import Ollama
#ollama_mixtral = Ollama(model="mixtral", base_url="http://localhost:11434")

# print(f">>>>>>>>model={os.environ['OPENAI_MODEL_NAME']}, base_url = {os.environ['OPENAI_API_BASE']}")
# exit()

@CrewBase
class TripPlannerCrew():
  """TripPlannerCrew crew"""
  agents_config = 'config/agents.yaml'
  tasks_config = 'config/tasks.yaml'
  
  def __init__(self) -> None:
    # self.llm_model = ChatGroq(temparature=0, model_name="mixtral-8x7b-32768")
    # self.llm_model = ollama_mixtral
    self.llm_model = ChatOllama(model=os.environ['OPENAI_MODEL_NAME'], temperature=0.7, verbose=True)
    self.search_tool = DuckDuckGoSearchRun()
    self.web_tool = WebsiteSearchTool()
    
  @agent
  def city_selection_agent(self) -> Agent:
    return Agent(
      config = self.agents_config['city_selection_agent'],
      llm = self.llm_model,
      tools=[
          # SearchTool.search_internet,
          self.web_tool,
          # self.search_tool,
          # BrowserTool.scrape_and_summarize_website,
          BrowserTool().scrape_and_summarize_website,
      ]
    )
  
  @agent
  def local_expert(self) -> Agent:
    return Agent(
      config = self.agents_config['local_expert'],
      llm = self.llm_model,
      tools=[
          # SearchTool.search_internet,
          self.web_tool,
          # self.search_tool,
          # BrowserTool.scrape_and_summarize_website,
          BrowserTool().scrape_and_summarize_website,
      ],
    )
    
  @agent
  def travel_concierge(self) -> Agent:
    return Agent(
      config = self.agents_config['travel_concierge'],
      llm = self.llm_model,
      tools=[
          # SearchTool.search_internet,
          self.web_tool,
          # self.search_tool,
          # BrowserTool.scrape_and_summarize_website,
          BrowserTool().scrape_and_summarize_website,
          CalculatorTool.calculate,
      ],
    )
  
  @task
  def identify_task(self) -> Task:
    return Task(
      config = self.tasks_config['identify_task'],
      agent = self.city_selection_agent()
    )
  
  @task
  def gather_task(self) -> Task:
    return Task(
      config = self.tasks_config['gather_task'],
      agent = self.local_expert()
    )
    
  @task
  def plan_task(self) -> Task:
    return Task(
      config = self.tasks_config['plan_task'],
      agent = self.travel_concierge()
    )
    
  @crew
  def crew(self) -> Crew:
    """Creates the FinancialAnalystCrew crew"""
    return Crew(
      agents = self.agents,
      tasks = self.tasks,
      process = Process.sequential,
      verbose = 2
    )