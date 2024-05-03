"""
Сбор данных со всех карточек товара.

Соберите данные всех карточек товара всех категорий и со всех страниц тренажера
(всего 160шт).
Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию
из превью.
Сохраните данные в JSON файл с использованием указанных параметров.
"""


import json
import requests
from bs4 import BeautifulSoup


with requests.Session() as rs:
    for num in range(1, 6):
        for page in range(1, 5):
            response = rs.get(
                f'https://parsinger.ru/html/index{num}_page_{page}.html'
            )
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            names = [
                name
                .text
                .strip() for name in soup
                .find_all('a', class_='name_item')
            ]
            descriptions = [
                desc
                .text
                .split('\n') for desc in soup
                .find_all('div', class_='description')
            ]
            prices = [
                price.text for price in soup.find_all('p', class_='price')
            ]

            result_json = []

            for name, description, price in zip(names, descriptions, prices):
                item_list = [
                    x.split(':')[1].strip() for x in description if x
                ]
                if num == 1:
                    result_json.append({
                        'Наименование': name,
                        'Бренд': item_list[0],
                        'Тип': item_list[1],
                        'Материал корпуса': item_list[2],
                        'Технология экрана': item_list[3],
                        'Цена': price
                    })

                if num == 2:
                    result_json.append({
                        'Наименование': name,
                        'Бренд': item_list[0],
                        'Диагональ экрана': item_list[1],
                        'Материал корпуса': item_list[2],
                        'Разрешение экрана': item_list[3],
                        'Цена': price
                    })

                if num == 3:
                    result_json.append({
                        'Наименование': name,
                        'Бренд': item_list[0],
                        'Тип': item_list[1],
                        'Подключение к компьютеру': item_list[2],
                        'Игровая': item_list[3],
                        'Цена': price
                    })

                if num == 4:
                    result_json.append({
                        'Наименование': name,
                        'Бренд': item_list[0],
                        'Форм-фактор': item_list[1],
                        'Ёмкость': item_list[2],
                        'Объем буферной памяти': item_list[3],
                        'Цена': price
                    })

                if num == 5:
                    result_json.append({
                        'Наименование': name,
                        'Бренд': item_list[0],
                        'Тип подключения': item_list[1],
                        'Цвет': item_list[2],
                        'Тип наушников': item_list[3],
                        'Цена': price
                    })

            with open('items.json', 'a', encoding='utf-8') as file:
                json.dump(result_json, file, indent=4, ensure_ascii=False)
