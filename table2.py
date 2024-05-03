"""
Суммирование чисел из первого столбца таблицы.

Перейти на сайт и найти таблицу.
Произвести парсинг данных из первого столбца таблицы.
Суммировать все числа, найденные в первом столбце.
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/2/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
rows = table.find_all('tr')

first_column = 0

for row in rows[1:]:
    num = float(row.find('td').text)
    first_column += num

print(first_column)
