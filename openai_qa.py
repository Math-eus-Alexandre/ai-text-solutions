import openai
from documento import documento
from my_key_openai import my_key

openai.api_key = my_key

pergunta = "Qual a ultima versao do Office?"
prompt = f'Contexto: {documento}\nPergunta: {pergunta}\nResposta:'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Voce e um assistente util."},
        {"role": "system", "content": prompt},         
    ],
    max_tokens = 100,
    temperature= 0.0
)

resposta = response['choices'] [0] ['message'] ['content'].strip()
print(f'Resposta: {resposta}')