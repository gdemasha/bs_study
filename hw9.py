"""
Открываем сайт
Получаем данные при помощи bs4 о старой цене и новой цене
По формуле высчитываем процент скидки
Формула (старая цена - новая цена) * 100 / старая цена)
Ответ должен быть числом с 1 знаком после запятой.
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/html/hdd/4/4_1.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

price = int(soup.find('span', id='price').text.rstrip(' руб'))
old_price = int(soup.find('span', id='old_price').text.rstrip(' руб'))

discount = (old_price - price) * 100 / old_price
print(f'{discount:.1f}')
