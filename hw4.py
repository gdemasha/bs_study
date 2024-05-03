"""
Проанализируйте страницу, определите тег и его атрибуты, затем
примените метод .find_all(), извлеките из каждого соответствующего
тега текст и уберите лишние пробелы.
Проанализируйте структуру сайта, найдите способ получить все цены
с помощью .find_all(), затем суммируйте их.
Проанализируйте страницу и найдите способ извлечь все ID из каждого
тега <li> (используйте select() или find_all()).
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

tags = soup.find_all('a', class_='name_item product_name')
for tag in tags:
    print(tag.text.strip())

prices = soup.find_all('p', class_='price product_price')
count = 0
for price in prices:
    count += int(price.text.replace(" ", "").rstrip('руб'))

print(count)

tags_li = soup.find_all('li')
for tag in tags_li:
    print(tag['id'])
