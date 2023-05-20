from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from time import sleep
import pandas as pd

url = "https://www.americanas.com.br/busca/tv-smart?rc=tv%20smart%20&=24&=20&=24&=&limit=24&offset=0"

# 1. ABRINDO O NAVEGADOR
driver = webdriver.Chrome()
driver.get(url)
sleep(2)

# 1.1 dicionarios

dict_produtos = {'televisores': [], 'valores': []}


for next in range(13):
    proxima_pagina = '//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div/ul/li[10]/button'
    some = '//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[2]'

    driver.find_element(By.XPATH, proxima_pagina).click()
    sleep(0.1)

    element = driver.find_element(By.XPATH, some)
    sleep(0.1)

    html_content = element.get_attribute('outerHTML')
    soup = bs(html_content, 'html.parser')
    produto = soup.find_all('div', class_='inStockCard__Wrapper-sc-1ngt5zo-0 iRvjrG')

    for p in produto:
        product = p.find('h3', class_='product-name__Name-sc-1shovj0-0 gUjFDF').get_text().strip()
        mercadoria = p.find('span',
                            class_='src__Text-sc-154pg0p-0 price__PromotionalPrice-sc-h6xgft-1 ctBJlj price-info__ListPriceWithMargin-sc-1xm1xzb-2 liXDNM').get_text().strip()
        sleep(0.1)

        print(product, mercadoria)

        dict_produtos['televisores'].append(product)
        dict_produtos['valores'].append(mercadoria)



df = pd.DataFrame(dict_produtos)
df.to_csv('C:/Users/Usuário/Downloads/Americanastv.csv', encoding='utf-8')