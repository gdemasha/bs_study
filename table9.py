"""
Поиск подходящих авто.

Запрашивайте данные с веб-сайта, который содержит таблицу автомобилей.
Фильтруйте автомобили по заданным критериям:
- Cтоимость не выше 4 000 000 (Стоимость авто <= 4000000),
- Год выпуска начиная с 2005 года (Год выпуска >= 2005),
- Тип двигателя - Бензиновый (Тип двигателя == "Бензиновый").
Выводите результат в формате JSON.
Сортируйте отфильтрованный JSON автомобилей по стоимости от меньшего
к большему.
"""


import json
import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.8/6/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

filtered_cars = []

table = soup.find('table')
headers = [header.text for header in table.find_all('th')]
key_headers = [headers[0], headers[1], headers[4], headers[-1]]
rows = table.find_all('tr')[1:]

for row in rows:
    cells = [cell.text for cell in row.find_all('td')]
    value_cells = [cells[0], int(cells[1]), cells[4], int(cells[-1])]
    if (
        value_cells[-1] <= 4000000
        and value_cells[1] >= 2005
        and value_cells[2] == 'Бензиновый'
    ):
        row_data = dict(zip(key_headers, value_cells))
        if row_data not in filtered_cars:
            filtered_cars.append(row_data)
    continue

sorted_cars = sorted(filtered_cars, key=lambda x: x["Стоимость авто"])
sorted_json = json.dumps(sorted_cars, indent=4, ensure_ascii=False)

print(sorted_json)
