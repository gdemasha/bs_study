"""
Извлечение и суммирование данных из таблицы в объединённых ячейках.

Загрузить страницу на которой расположена таблица с объединёнными ячейками.
Извлечь данные из каждой объединённой ячейки(всего 16 ячеек),
объединённую ячейку можно определить по атрибуту colspan.
Суммировать все числовые значения, полученные из объединённых ячеек.
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.8/8/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

total_colspan = 0
all_cells = []

table = soup.find('table')

for i in range(2, 6):
    if not i == 3:
        cells = [
            int(cell.text) for cell in table.find_all(
                attrs={'colspan': f'{i}'},
            )
        ]
        total_colspan += sum(cells)

cells_3 = [
    int(cell.text) for cell in table.find_all(
        attrs={'colspan': '3'},
    )[1:]
]
total_colspan += sum(cells_3)

print(total_colspan)
