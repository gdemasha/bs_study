"""
Открываем сайт
Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт)
Складываем все числа
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/html/index1_page_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

total_price = 0
prices = soup.find_all('p', class_='price')

for price in prices:
    clean_price = int(price.text.rstrip(' руб'))
    total_price += clean_price

print(total_price)
