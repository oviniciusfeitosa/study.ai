import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json
from unstructured.partition.html import partition_html
from langchain.tools import tool
from langchain_community.chat_models import ChatOllama
# from crewai import Agent, Task
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts.prompt import PromptTemplate


llm_model = ChatOllama(model=os.environ['OPENAI_MODEL_NAME'], temperature=0.7, verbose=True)

class BrowserTool():
  
  agents_config = '../config/agents.yaml'
  tasks_config = '../config/tasks.yaml'
  
  def __init__(self) -> None:
    # self.llm_model = ChatOllama(model=os.environ['OPENAI_MODEL_NAME'], base_url = "http://localhost:11434")
    self.llm_model = ChatOllama(model=os.environ['OPENAI_MODEL_NAME'], temperature=0.7, verbose=True)

  def search_website(self, website_url) -> str:
    """Useful to scrape a website content. Expect `website_url` to be a valid url."""
    # url = f"https://chrome.browserless.io/content?token={os.environ['BROWSERLESS_API_KEY']}"
    url = "http://localhost:3000/content"
    payload = json.dumps({"url": website_url})
    headers = {'cache-control': 'no-cache', 'content-type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    elements = partition_html(text=response.text)
    content = "\n\n".join([str(el) for el in elements])
    # content = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    # summaries = []
    # for chunk in content:
        # agent = Agent(
        #     config = self.agents_config['website_content_summarizer'],
        # )
        # task = Task(
        #     config = self.tasks_config['summarize_task'],
        #     description = f'''
        #       Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.
              
        #       CONTENT:
        #       ----------
        #       {chunk}
        #     ''',
        #     agent = agent,
        #     # context = []
        # )
        # summary = task.execute()
        
        
        # summaries.append(summary)
    # return "\n\n".join(summaries)
    return content

  # def summary(self, objective, content) -> str:
  def summary(self, content) -> str:
    """Useful to summarize content. Expect `content` to be a string."""
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n"], chunk_size=10000, chunk_overlap=500)
    content_splited = [content[i:i + 8000] for i in range(0, len(content), 8000)]
    docs = text_splitter.create_documents(content_splited)
    # docs = text_splitter.create_documents([content])
    
    # 1
    # map_prompt = """
    # Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.
    # CONTENT:
    # ----------
    # {text}
    # """
    
    # map_prompt_template = PromptTemplate(
    #     # template=map_prompt, input_variables=["content", "objective"])
    #     template=map_prompt, input_variables=["text"])

    # summary_chain = load_summarize_chain(
    #     llm=llm_model,
    #     chain_type='map_reduce',
    #     # chain_type='REFINE',
    #     map_prompt=map_prompt_template,
    #     combine_prompt=map_prompt_template,
    #     verbose=True
    # )
    # # return summary_chain.run(input_documents=docs)
    
    # 2
    # summary_chain = load_summarize_chain(
    #     llm_model,
    #     chain_type='map_reduce',
    #     verbose=False
    # )

    # return summary_chain.run(docs)
    
    # 3
    map_prompt = """
      Analyze and summarize the content bellow, make sure to include the most relevant information in the summary, return only the summary nothing else.
      CONTENT:
      {text}
      ----------
      SUMMARY:
    """
    map_prompt_template = PromptTemplate(template=map_prompt, input_variables=["text"])
    summary_chain = load_summarize_chain(
        llm=self.llm_model,
        chain_type='map_reduce',
        # chain_type='REFINE',
        map_prompt=map_prompt_template,
        combine_prompt=map_prompt_template,
        verbose=True
    )
    
    summary = summary_chain.invoke(docs)
    # print(summary)
    return summary
  
  @tool("Scrape and summarize website content")
  def scrape_and_summarize_website(self, website_url: str) -> str:
    """Useful to scrape and summarize a website content. Expect `website_url` to be a valid url."""
    content = self.search_website(website_url)
    return self.summary(content)
  