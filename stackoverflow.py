import requests
from bs4 import BeautifulSoup

url = 'https://pt.stackoverflow.com/questions/tagged/python'

response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.s-post-summary--content'):
    data = pergunta.select_one('.relativetime')
    head = pergunta.select_one('.s-link')
    print(data.text, head.text, sep='\t')