
import os
from embedchain import App
from dotenv import load_dotenv
load_dotenv()
# os.environ["HUGGINGFACE_ACCESS_TOKEN"] = "xxx"
print(f'os.environ["HUGGINGFACE_ACCESS_TOKEN"]: {os.environ["HUGGINGFACE_ACCESS_TOKEN"]}')
config = {
  "app": {"config": {"id": "my-app"}},
  "llm": {
      "provider": "huggingface",
      "config": {
          "model": "bigscience/bloom-1b7",
          "top_p": 0.5,
          "temperature": 0.1,
          "stream": False,
      },
      
  },
  "embedder": {
        "provider": "huggingface",
        "config": {
            "model": "BAAI/bge-large-zh-v1.5",
        },
    },
}

app = App.from_config(config=config)
app.add("avaliacao.json")

print(app.query("Qual o mais caro?"))