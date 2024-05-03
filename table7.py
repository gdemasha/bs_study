"""
Суммирование чисел, кратных трём, из шести таблиц.

Загрузить страницу с шестью таблицами.
Пройтись по каждой ячейке каждой таблицы и проверить значение
на кратность трём.
Если число кратно трем, добавить его к общей сумме.
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.8/7/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

total = 0

tables = soup.find_all('table')

for table in tables:
    cells = [int(cell.text) for cell in table.find_all('td')]
    for cell in cells:
        if cell % 3 == 0:
            total += cell
        continue

print(total)
