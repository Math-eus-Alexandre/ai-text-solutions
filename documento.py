import requests
from bs4 import BeautifulSoup

def extraindo_texto_da_web(url):
    response = requests.get(url)
    response.raise_for_status() # verifica se o request foi bem-sucedido
    soup = BeautifulSoup(response.text, 'html.parser')

    # extrai todo o texto visivel da pagina
    paragraphs = soup.find_all('p')
    text = " ".join([para.get_text() for para in paragraphs])
    return text

url = "https://pt.wikipedia.org/wiki/Microsoft_Office"

documento = extraindo_texto_da_web(url)

if __name__ == '__main__':
    print(documento)