"""
Сбор данных о HDD в JSON.

Соберите данные о HDD с четырёх страниц в категории HDD.
Не "проваливайтесь" внутрь каждой карточки.
Соберите только информацию из превью.
Сохраните данные в JSON файл с использованием указанных параметров.
"""

import json
import requests
from bs4 import BeautifulSoup


for num in range(1, 5):
    response = requests.get(
        f'https://parsinger.ru/html/index4_page_{num}.html'
    )
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    names = [
        name.text.strip() for name in soup.find_all('a', class_='name_item')
    ]
    descriptions = [
        desc.text.split('\n') for desc in soup.find_all(
            'div', class_='description'
        )
    ]
    prices = [price.text for price in soup.find_all('p', class_='price')]

    result_json = []

    for name, description, price in zip(names, descriptions, prices):
        item_list = [x.split(':')[1].strip() for x in description if x]
        result_json.append({
            'Наименование': name,
            'Бренд': item_list[0],
            'Форм-фактор': item_list[1],
            'Ёмкость': item_list[2],
            'Объем буферной памяти': item_list[3],
            'Цена': price
        })

    with open('hdd.json', 'a', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)
