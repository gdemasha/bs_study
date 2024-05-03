"""
Анализ количества товаров через JSON.

Вашей задачей является обработка данных в формате JSON, полученных по ссылке​.
Для подсчета общего количества товаров в разных категориях.
Каждая карточка товара содержит информацию о количестве данного товара.
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
    items_count[item['categories']] += int(item['count'])

print(items_count)
