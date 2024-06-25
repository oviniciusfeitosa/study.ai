from crewai import Agent, Task, Crew, Process
from langchain_community.llms import Ollama

# from llama_index.legacy.llms.ollama import Ollama


# from langchain_openai import ChatOpenAI
# from langchain_community.tools import DuckDuckGoSearchRun
# from crewai_tools import WebsiteSearchTool
from crewai_tools import JSONSearchTool
import sys
import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OLLAMA_HOST"] = "http://127.0.0.1:11434"
# search_tool = DuckDuckGoSearchRun()
# web_tool = WebsiteSearchTool()


llm = Ollama(model="mistral:7b", verbose=True)
# llm  = ChatOpenAI(temperature=0.1, model="gpt-3.5-turbo")


def kickoffTheCrew(topic):
    json_path = (
        "./data/avaliacao.json"
    )
    researcher = Agent(
        role="Document Research",
        goal=f"Perform research on the {topic}, and find and explore about {topic} ",
        verbose=True,
        llm=llm,
        backstory="""You are an expert Document Researcher who knows how to search the Document for detailed content on {topic} Include any code examples with documentation""",
        # tools=[
        #     JSONSearchTool(
        #         json_path=json_path,
        #         config=dict(
        #             llm=dict(
        #                     # embedchain.llm.ollama.OllamaLlm
        #                 provider="ollama",  # Other options include google, openai, anthropic, llama2, etc.
        #                 config=dict(
        #                     model="llama2",
        #                     # Additional optional configurations can be specified here.
        #                     temperature=0.5,
        #                     top_p=1,
        #                     stream=True,
        #                 ),
        #             ),
        #             embedder=dict(
        #                 # embedchain.embedder.huggingface.HuggingFaceEmbedder
        #                 # embedchain.config.embedder.ollama.OllamaEmbedderConfig
        #                 provider="huggingface",
        #                 config=dict(
        #                     model="BAAI/bge-small-en-v1.5",
        #                     # "task_type": "retrieval_document" #where can I see task_type?
        #                 ),
        #             ),
        #         ),
        #     )
        # ],
    )

    task_search = Task(
        description="""Search for all the details about the  {topic}. Your final answer MUST be a consolidated content that can be used to be synthetized. This content should be well organized, and should be very easy to read""",
        expected_output="A comprehensive 10000 words information about {topic}",
        max_inter=3,
        tools=[
            JSONSearchTool(
                json_path=json_path,
                config=dict(
                    llm=dict(
                            # embedchain.llm.ollama.OllamaLlm
                        provider="ollama",  # Other options include google, openai, anthropic, llama2, etc.
                        config=dict(
                            # model="llama2",
                            model="mistral:7b",
                            # Additional optional configurations can be specified here.
                            temperature=0.5,
                            top_p=1,
                            stream=True,
                        ),
                    ),
                    embedder=dict(
                        # embedchain.embedder.huggingface.HuggingFaceEmbedder
                        # embedchain.config.embedder.ollama.OllamaEmbedderConfig
                        provider="huggingface",
                        config=dict(
                            model="BAAI/bge-small-en-v1.5",
                            # "task_type": "retrieval_document" #where can I see task_type?
                        ),
                    ),
                ),
            )
        ],
        agent=researcher,
    )

    crew = Crew(
        agents=[researcher], tasks=[task_search], verbose=2, process=Process.sequential
    )

    result = crew.kickoff()
    return result


n = len(sys.argv)

# print(f"sys.argv = {sys.argv}")

if n > 1:
    # Get the argumens after `main.py` as text to `topic` var
    topic = " ".join(sys.argv[1:])
    # topic = sys.argv[1]
    result = kickoffTheCrew(topic)
    print(result)
else:
    print("Please pass topic as parameter. Usage python3 main2.py \"topic\"")
