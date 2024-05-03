"""
Комплексное извлечение стоимости товаров.

Цель: Посетить указанный веб-сайт, систематически пройти по всем категориям,
страницам и карточкам товаров (всего 160 шт.). Из каждой карточки товара
извлечь стоимость и умножить ее на количество товара в наличии.
Полученные значения агрегировать для вычисления общей стоимости всех
товаров на сайте.
"""


from bs4 import BeautifulSoup
import requests
import time


start = time.time()

with requests.Session() as rs:
    response = rs.get('https://parsinger.ru/html/index1_page_1.html')
    soup = BeautifulSoup(response.text, 'html.parser')
    navs = [
        nav['href'] for nav in soup
        .find('div', class_='nav_menu')
        .find_all('a')
    ]

    base_url = 'https://parsinger.ru/html/'
    nav_urls = [f'{base_url}{nav}' for nav in navs]
    price_for_all = 0

    for url in nav_urls:
        response = rs.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [
            link['href'] for link in soup
            .find('div', class_='pagen')
            .find_all('a')
        ]
        pages = [f'{base_url}{link}' for link in links]

        for page in pages:
            response = rs.get(page)
            soup = BeautifulSoup(response.text, 'html.parser')
            sale_buttons = soup.find_all('div', class_='sale_button')
            item_links = [button.find('a')['href'] for button in sale_buttons]

            for item in item_links:
                response = rs.get(f'{base_url}{item}')
                response.encoding = 'utf-8'
                soup = BeautifulSoup(response.text, 'html.parser')
                in_stock = int(
                    soup
                    .find('span', id='in_stock')
                    .text
                    .lstrip('В наличии: ')
                )
                price = int(soup.find('span', id='price').text.rstrip(' руб'))
                total_price = in_stock * price
                price_for_all += total_price

stop = time.time()
t = stop - start

print(price_for_all)
print(t)
