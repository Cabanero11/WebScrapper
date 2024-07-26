import requests
import os
from bs4 import BeautifulSoup

# Solo funciona con paginas estaticas que devuelvan .html 
url = 'https://realpython.github.io/fake-jobs/'

pagina = requests.get(url)

soup = BeautifulSoup(pagina.content, 'html.parser')

trabajos = soup.find(id='ResultsContainer')

trabajos_post = trabajos.find_all('div', class_='card-content')

# Filtro que tenga python PyThoN (todo lowercase asi se consigue todo)
python_trabajos = trabajos.find_all(
    'h2', string=lambda texto:'python' in texto.lower()
)

# Conseguir el elementos 3 arriba del h2 (el titulo)
python_trabajos_elementos = [
    h2.parent.parent.parent for h2 in python_trabajos
]

#print(python_trabajos_elementos[0])

try:
    with open ('scrap.txt', 'w') as file:
        for trabajo in python_trabajos_elementos:
            titulo = trabajo.find('h2', class_='title').text.strip()
            compañia = trabajo.find('h3', class_='company').text.strip()
            localizacion = trabajo.find('p', class_='location').text.strip()
            file.write(f'Titulo: {titulo}\n')
            file.write(f'Compania: {compañia}\n')
            file.write(f'Localizacion: {localizacion}\n\n')
except FileNotFoundError as e:
    print(f'Error -> {e}')

    print("Scrappeacion guardada en 'scrap.txt'")