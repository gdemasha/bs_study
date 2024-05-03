"""
Извлечение всех email со страницы.

Проанализируйте предоставленный HTML-код страницы.
Ваша задача - обнаружить и извлечь все email-адреса,
которые находятся вне стандартных тегов.
Вам предстоит модифицировать функцию ниже таким образом,
чтобы она возвращала список всех найденных email-адресов,
очищенных от лишних пробелов с помощью метода strip().
Ваша функция должна возвращать список email-адресов в чистом виде,
готовых к дальнейшему использованию.
"""


from bs4 import BeautifulSoup
import requests


response = requests.get('https://parsinger.ru/4.1/1/index5.html')
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

email_list = []
emails = soup.select('div.email_field strong')

for line in emails:
    email = line.next_sibling.strip()
    email_list.append(email)

print(email_list)
