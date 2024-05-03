"""
Агрегация выделенных чисел из таблицы.

Перейти на сайт и обнаружить требуемую таблицу.
Cобрать только числа, отформатированные жирным шрифтом.
Суммировать выделенные числа.
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/3/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

table = soup.find('table')
nums = [float(num.text) for num in table.find_all('b')]
print(sum(nums))
