# Requisições para os sites 
import requests 
# Traduzir a resposta 
from bs4 import BeautifulSoup

# URL para acesso
url = "https://g1.globo.com/"

# Fazendo a requisição
resposta = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if resposta.status_code == 200:
    # Traduzir a resposta
    soup = BeautifulSoup(resposta.text, "html.parser")

    # Coletar os links de notícias
    noticias = soup.find_all("a", class_="feed-post-link")

    # Exibir as manchetes encontradas
    for index, noticia in enumerate(noticias, 1):
        print(f"{index+1}. {noticia.text.strip()}")
        print(f"   Link: {noticia['href']}")
else:
    print(f"Erro ao acessar o site: {resposta.status_code}")
