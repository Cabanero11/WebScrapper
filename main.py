import requests
import os
from bs4 import BeautifulSoup

# Solo funciona con paginas estaticas que devuelvan .html 
url = 'https://realpython.github.io/fake-jobs/'

pagina = requests.get(url)

soup = BeautifulSoup(pagina.content, 'html.parser')

trabajos = soup.find(id='ResultsContainer')

trabajos_post = trabajos.find_all('div', class_='card-content')

try:
    with open ('trabajos.txt', 'w') as file:
        for trabajo in trabajos_post:
            titulo = trabajo.find('h2', class_='title')
            compañia = trabajo.find('h3', class_='company')
            localizacion = trabajo.find('p', class_='location')
            file.write(titulo.text.strip() + '\n')
            file.write(compañia.text.strip() + '\n')
            file.write(localizacion.text.strip() + '\n' * 2)
except FileNotFoundError as e:
    print(f'Error -> {e}')