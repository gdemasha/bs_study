"""
Извлечение названий товаров с веб-сайта.

Цель: Посетить указанный веб-сайт и извлечь названия товаров со всех четырех
страниц. Необходимо организовать данные таким образом, чтобы названия товаров
с каждой страницы хранились в отдельном списке.
По завершении работы у вас должен быть главный список, содержащий четыре
вложенных списка с названиями товаров.
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/html/index3_page_1.html')
soup = BeautifulSoup(response.text, 'html.parser')

links = [
    link['href'] for link in soup.find('div', class_='pagen').find_all('a')
]
base_url = 'https://parsinger.ru/html/'
urls = [f'{base_url}{link}' for link in links]

names_list = []

for url in urls:
    response = requests.get(url=url)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    names = [name.text for name in soup.find_all('a', 'name_item')]
    names_list.append(names)

print(names_list)
