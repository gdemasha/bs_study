"""
Суммирование чисел из зелёных ячеек таблицы.

Открыть веб-сайт и найти целевую таблицу.
Провести анализ данных в таблице, фокусируясь на ячейках зелёного цвета.
Выделить и подсчитать сумму всех чисел из зелёных ячеек.
Данные должны иметь следующий вид: ***.7659999999999
"""


import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/table/4/index.html')
soup = BeautifulSoup(response.text, 'html.parser')

green_cells = soup.find('table').find_all('td', class_='green')
nums = [float(num.text) for num in green_cells]
print(sum(nums))
