"""
Парсинг артикулов товаров с веб-сайта.

Цель: Посетить указанный веб-сайт, пройти по всем страницам в категории 'мыши'
и из каждой карточки товара извлечь артикул. После чего все извлеченные
артикулы необходимо сложить и представить в виде одного числа.
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/html/index3_page_1.html')
soup = BeautifulSoup(response.text, 'html.parser')

links = [link['href'] for link in soup.find('div', 'pagen').find_all('a')]
base_url = 'https://parsinger.ru/html/'
urls = [f'{base_url}{link}' for link in links]

article_count = 0

for url in urls:
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    sale_buttons = soup.find_all('div', class_='sale_button')
    item_links = [button.find('a')['href'] for button in sale_buttons]

    for item in item_links:
        response = requests.get(f'{base_url}{item}')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        article = int(
            soup.find('p', class_='article').text.lstrip('Артикул: ')
        )
        article_count += article

print(article_count)
