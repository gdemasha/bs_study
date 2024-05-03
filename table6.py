"""
Агрегация данных из столбцов таблицы в словарь.

Открыть веб-сайт и обнаружить интересующую таблицу.
Для каждого столбца вычислить сумму всех чисел в этом столбце.
Округлить каждое получившееся значение до трех знаков после запятой.
Формировать словарь, где ключами будут названия столбцов,
а значениями - рассчитанные суммы.
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

columns = {}

for i in range(15):
    columns[f'{i+1} column'] = 0

rows = soup.find('table').find_all('tr')
for row in rows[1:]:
    cells = [float(cell.text) for cell in row.find_all('td')]
    for i in range(0, len(cells)):
        columns[f'{i+1} column'] += cells[i]

for key, value in columns.items():
    columns[key] = round(value, 3)

print(columns)
