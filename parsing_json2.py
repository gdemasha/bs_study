"""
Вычисление Стоимости Товаров в Каждой Категории.

Обработайте JSON-структуру по ссылке, которая содержит информацию
о товарах разных категорий. Ваша цель - рассчитать общую стоимость
в каждой из этих категорий.
"""


import requests

url = 'http://parsinger.ru/downloads/get_json/res.json'

response = requests.get(url=url).json()

items_count = {
    'watch': 0,
    'mobile': 0,
    'mouse': 0,
    'hdd': 0,
    'headphones': 0
}

for item in response:
    total = int(item['count']) * int(item['price'].strip(' руб'))
    items_count[item['categories']] += total

print(items_count)
