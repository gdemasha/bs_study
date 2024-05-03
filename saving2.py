"""
Сбор данных о часах с карточек товара.

Изучите указанную страницу для получения информации
о часах с четырёх страниц в разделе "ЧАСЫ".
Вам потребуется заходить в каждую товарную карточку и
собирать данные, отмеченные на предоставленном изображении.
"""


import csv
import requests
from bs4 import BeautifulSoup


with open('watches.csv', 'w', encoding='utf-8-sig', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(
        [
            'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип',
            'Технология экрана', 'Материал корпуса', 'Материал браслета',
            'Размер', 'Сайт производителя', 'Наличие', 'Цена',
            'Старая цена', 'Ссылка на карточку с товаром',
        ]
    )

base_url = 'https://parsinger.ru/html/'

for page in range(1, 5):
    with requests.Session() as rs:
        response = rs.get(f'https://parsinger.ru/html/index1_page_{page}.html')
        soup = BeautifulSoup(response.text, 'lxml')

        item_hrefs = [
            button.find('a')['href'] for button in soup.find_all(
                'div', class_='sale_button'
            )
        ]
        item_urls = [f'{base_url}{href}' for href in item_hrefs]

        for url in item_urls:
            response = rs.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            name = soup.find('p', id='p_header').text
            article = (
                soup
                .find('p', class_='article')
                .text
                .split(':')[1]
                .strip()
            )
            brand = (
                soup
                .find('li', id='brand')
                .text
                .split(':')[1]
                .strip()
            )
            model = (
                soup
                .find('li', id='model')
                .text
                .split(':')[1]
                .strip()
            )
            con_type = (
                soup
                .find('li', id='type')
                .text
                .split(':')[1]
                .strip()
            )
            display = (
                soup
                .find('li', id='display')
                .text
                .split(':')[1]
                .strip()
            )
            material_frame = (
                soup
                .find('li', id='material_frame')
                .text
                .split(':')[1]
                .strip()
            )
            material_bracer = (
                soup
                .find('li', id='material_bracer')
                .text
                .split(':')[1]
                .strip()
            )
            size = soup.find('li', id='size').text.split(':')[1].strip()
            site = (
                soup
                .find('li', id='site')
                .text
                .split(':')[1]
                .strip()
            )
            stock = soup.find('span', id='in_stock').text.split(':')[1].strip()
            price = soup.find('span', id='price').text
            old_price = soup.find('span', id='old_price').text

            with (
                open(
                    'watches.csv', 'a', encoding='utf-8-sig', newline=''
                ) as file
            ):
                writer = csv.writer(file, delimiter=';')
                row = (
                    name, article, brand, model, con_type,
                    display, material_frame, material_bracer,
                    size, site, stock, price, old_price, url,
                )
                writer.writerow(row)

print('Файл watches.csv создан')
