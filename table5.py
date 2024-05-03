"""
Агрегация произведений чисел из оранжевых и голубых ячеек таблицы.

Открыть веб-сайт и обнаружить необходимую таблицу.
Для каждой строки таблицы найти числа в оранжевой и голубой ячейках,
после чего умножить их друг на друга.
Сложить все получившиеся произведения, чтобы получить общую сумму.
Данные должны иметь следующий вид: *******.6860000016
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/5/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

total = 0

rows = soup.find('table').find_all('tr')

for row in rows[1:]:
    orange = float(row.find('td', class_='orange').text)
    blue = int(row.find_all('td')[-1].text)
    multiply = orange * blue
    total += multiply

print(total)
