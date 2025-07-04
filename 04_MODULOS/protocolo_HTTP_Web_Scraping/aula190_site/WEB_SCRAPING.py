# Web Scraping com Python usando requests e bs4 BeautifulSoup

# Web Scraping é o ato de "raspar a web" buscando informações de forma automatizada,
# com determinada linguagem de programação, para uso posterior.

# O módulo requests consegue carregar dados da Internet para dentro do seu código.
# Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML em formato de 
# objetos Python para facilitar a vida do desenvolvedor.

# pip install requests types-requests bs4

import re
import requests
from bs4 import BeautifulSoup

url='http://localhost:3333/'
response = requests.get(url)

raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

# Acessando a tag html(title) e o conteúdo(text)
if parsed_html.title is not None:
    print(parsed_html.title.text)


top_jobs_head = parsed_html.select_one('#intro > div > div > article > h2')
if top_jobs_head is not None:
    print(top_jobs_head.text)

    article = top_jobs_head.parent
    print(article)

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' '. p.text).strip())
