import openai
from documento import documento
from my_key_openai import my_key

openai.api_key = my_key


prompt = f'Resuma o seguinte texto de forma abstrativa:\n{documento}'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Voce e um assistente que pode resumir textos."},
        {"role": "system", "content": prompt},         
    ],
    max_tokens = 100,
    temperature= 0.7
)

resumo = response['choices'] [0] ['message'] ['content'].strip()
print(f'Resumo: {resumo}')