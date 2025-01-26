import openai
from my_key_openai import my_key

openai.api_key = my_key

texto = "Esta chovendo forte aqui em Brusque, estou com medo"
prompt = f'Classifique o sentimento do seguinte texto como "Positivo", "Negativo" ou "Neutro":\n{texto}'

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Voce e um assistente util."},
        {"role": "system", "content": prompt},         
    ],
    max_tokens = 60,
    temperature= 0.0
)

sentimento = response['choices'] [0] ['message'] ['content'].strip()
print(f'Sentimento: {sentimento}')