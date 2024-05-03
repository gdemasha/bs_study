"""
Сбор данных о HDD.

Используйте страницу чтобы собрать данные с
четырёх страниц в категории hdd.
"Проваливаться" в каждую карточку не нужно,
соберите информацию с превью карточки.
"""


import csv
import requests
from bs4 import BeautifulSoup


with open('hdd.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        [
            'Наименование', 'Бренд', 'Форм-фактор',
            'Ёмкость', 'Объем буферной памяти', 'Цена',
        ]
    )

for num in range(1, 5):
    response = requests.get(
        f'https://parsinger.ru/html/index4_page_{num}.html'
    )
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')

    names = [
        name.text.strip() for name in soup.find_all('a', class_='name_item')
    ]
    prices = [price.text for price in soup.find_all('p', class_='price')]
    descriptions = [
        descr.text.split('\n') for descr in soup.find_all(
            'div', class_='description'
        )
    ]

    with open('hdd.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for name, descr, price in zip(names, descriptions, prices):
            row = (
                name,
                *[item.split(':')[1].strip() for item in descr if item],
                price,
            )
            writer.writerow(row)

print('Файл hdd.csv создан')
