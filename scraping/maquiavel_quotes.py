from bs4 import BeautifulSoup
import requests


url = "https://www.pensador.com/frases_de_maquiavel/"


response  = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
conteiner = soup.find(class_='phrases-list')
items = conteiner.find_all('p')

for item in items:
    print(item.text)
