"""
Вычисление Произведения 'article' и 'rating'.

Получение данных: Используйте инструменты разработчика для
определения источника данных(вкладка Network).
Обработка данных: Извлеките данные со страницы и создайте словарь,
в котором для каждой карточки вычислите произведение значений
"article" и "rating".
Сбор значений: Суммируйте результаты произведений для каждой категории.
Формирование словаря: Завершая задачу, создайте словарь, в котором
ключами будут категории, а значениями - суммы произведений
"article" и "rating".
"""

import requests

url = 'https://parsinger.ru/4.6/1/res.json'

response = requests.get(url=url).json()

items_count = {
    'watch': 0,
    'mobile': 0,
    'mouse': 0,
    'hdd': 0,
    'headphones': 0
}

for item in response:
    total = int(item['article']) * int(item['description']['rating'])
    items_count[item['categories']] += total

print(items_count)
