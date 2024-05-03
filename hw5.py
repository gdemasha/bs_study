"""
Проанализируйте HTML на странице и извлеките из него текст
находящийся после третьего раздела.
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/4.1/1/index6.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

section3 = soup.select_one('#section3')
sibling = section3.find('p', class_='section-text').next_sibling.strip()
print(sibling)
