from dotenv import load_dotenv
load_dotenv()
from embedchain import App

app = App.from_config(config_path="ollama_embedchain.yaml")
print(app)
print("Start")
app.add(source='./data/avaliacao.json')



# print(app.query("Qual a média de preços?"))
print(app.query("Imagine que você é um especialista em análise de preços. Seu objetivo é fornecer respostas precisas e completas à partir dos dados que você tem acesso. Responda de forma sucinta, começando com a frase 'De acordo com os dados fornecidos a resposta é:', mostre o que o levou a chegar a essa resposta e tenha certeza que a resposta esteja correta. Qual a média de preços para o `uf` DF?"))