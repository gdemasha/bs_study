"""
Агрегация уникальных данных из таблицы.

Перейти на сайт и найти таблицу.
Произвести парсинг данных из таблицы.
Отфильтровать и извлечь все уникальные числа, исключая числа
в заголовке таблицы.
Посчитать сумму этих чисел.
Данные должны иметь следующий вид: ***.0959999999998
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/1/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

unique_nums = []

table = soup.find('table')
rows = table.find_all('tr')

for row in rows[1:]:
    cells = row.find_all('td')
    for cell in cells:
        if float(cell.text) not in unique_nums:
            unique_nums.append(float(cell.text))
        continue

result = sum(unique_nums)
print(result)
