from bs4 import BeautifulSoup as bs
import re
import requests

url = "https://www.brainyquote.com/authors/barack-obama-quotes"

headers = {
    'User Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (HTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"}

site = requests.get(url, headers=headers)

soupa = bs(site.content, 'html.parser')

quotes_mother = soupa.find_all('div', class_='grid-item qb clearfix bqQt')

quotes = soupa.find('a', class_=re.compile('oncl_q'))

for q in quotes_mother:
    speaks = q.find('a', class_=re.compile('oncl_q')).get_text().strip()
    print(speaks)