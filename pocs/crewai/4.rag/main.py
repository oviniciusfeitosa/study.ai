from dotenv import load_dotenv
load_dotenv()
# from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import (VectorStoreIndex, SimpleDirectoryReader, Settings, PromptTemplate)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from IPython.display import Markdown, display
documents = SimpleDirectoryReader("./data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
# Settings.llm = Ollama(model="llama3:latest", request_timeout=360.0)
Settings.llm = Ollama(model="mistral:7b", request_timeout=360.0)

index = VectorStoreIndex.from_documents(
    documents,
)
     

template = (
    "Imagine que você é um especialista em análise de preços. "
    "Seu objetivo é fornecer respostas precisas e completas à partir dos dados que você tem acesso."
    "Pergunta: {query_str}\n\n"
    "Responda de forma sucinta, começando com a frase 'De acordo com os dados fornecidos a resposta é:', mostre o que o levou a chegar a essa resposta e tenha certeza que a resposta esteja correta.\n\n"
    )
qa_template = PromptTemplate(template)
# Query
# query_engine = index.as_query_engine()
query_engine = index.as_query_engine(text_qa_template=qa_template, similarity_top_k=3)
response = query_engine.query("Qual a média de preços para o `uf` MS?")
print(response)

display(Markdown(f"response"))

# import logging
# import sys

# logging.basicConfig(stream=sys.stdout, level=logging.INFO)
# logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

# import os
# from dotenv import load_dotenv
# load_dotenv()

# # import openai

# # os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_KEY_HERE"
# # openai.api_key = os.environ["OPENAI_API_KEY"]
     

# from IPython.display import Markdown, display
     

# import json

# # Specify the folders containing the JSON and schema files
# json_folder = 'data2'
# schema_folder = 'data2'
     

# # Specify the filenames of the JSON and schema files
# json_filename = 'cake.json'
# schema_filename = 'schema.json'
     

# # Construct the paths to the JSON and schema files
# json_filepath = os.path.join(json_folder, json_filename)
# schema_filepath = os.path.join(schema_folder, schema_filename)
     

# # Read the JSON file
# with open(json_filepath, 'r') as json_file:
#     json_value = json.load(json_file)
     

# # Read the schema file
# with open(schema_filepath, 'r') as schema_file:
#     json_schema = json.load(schema_file)
     

# # from llama_index.indices.service_context import ServiceContext
# from llama_index.core import Settings
# # from llama_index.llms import OpenAI
# from llama_index.core.indices.struct_store import JSONQueryEngine
# from llama_index.llms.ollama import Ollama

# # llm = Ollama(model="llama3", request_timeout=360.0, )
# llm = Ollama(model="mistral:7b", request_timeout=360.0, )
# Settings.llm = llm

# # Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
# # Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=20)
# Settings.num_output = 512
# Settings.context_window = 3900

# nl_query_engine = JSONQueryEngine(
#     json_value=json_value, 
#     json_schema=json_schema,
#     llm=llm,
# )
# raw_query_engine = JSONQueryEngine(
#     json_value=json_value,
#     json_schema=json_schema,
#     llm=llm,
#     synthesize_response=False,
# )


# nl_response = nl_query_engine.query(
#     "What comments has Jerry been writing?",
# )
# raw_response = raw_query_engine.query(
#     "What comments has Jerry been writing?",
# )

# display(
#     Markdown(f"<h1>Natural language Response</h1><br><b>{nl_response}</b>")
# )
# display(Markdown(f"<h1>Raw JSON Response</h1><br><b>{raw_response}</b>"))
