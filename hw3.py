"""
Суммируйте атрибуты только у тегов <p> четной длины.

Цель: Написать код, который будет обрабатывать HTML-структуру,
состоящую из тегов <p>. Код должен анализировать текст внутри
каждого тега и, если количество символов в тексте (без учета пробелов)
является чётным, суммировать значения атрибутов id и class.
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/4.3/4/index.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
ps = soup.select('p')
total_id_sum = 0
total_class_sum = 0
for text in ps:
    if len(text.text.replace(" ", "")) % 2 == 0:
        total_id_sum += int(text['id'])
        total_class_sum += int(text['class'][0])
    continue

print(
    'Сумма ID и CLASS тегов <p> с чётной длиной текста без пробелов: '
    f'{total_id_sum + total_class_sum}'
)
