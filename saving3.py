"""
Сбор данных со всех карточек(160шт).

Соберите указанные на изображении ниже данные с сайта тренажёра.
Заходить в каждую карточку с товаром не требуется,
собирать необходимо только с превью карточки.
"""

import csv
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

            with open(
                'items.csv', 'a', encoding='utf-8-sig', newline=''
            ) as file:
                writer = csv.writer(file, delimiter=';')
                for name, description, price in zip(
                    names, descriptions, prices
                ):
                    row = (
                        name,
                        *[desc.split(':')[1]
                          .strip() for desc in description if desc
                          ],
                        price,
                    )
                    writer.writerow(row)
