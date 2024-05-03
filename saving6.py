"""
Сбор данных о телефонах с карточек товара.

Соберите данные из категории mobile  (всего 32 карточки).
"Провалитесь" в каждую карточку и соберите необходимую информацию.
Сохраните данные в JSON файл с использованием указанных параметров.
"""


import json
import requests
from bs4 import BeautifulSoup


base_url = 'https://parsinger.ru/html/'

for page in range(1, 5):
    with requests.Session() as rs:
        response = rs.get(f'https://parsinger.ru/html/index2_page_{page}.html')
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        item_hrefs = [
            link['href'] for link in soup.find_all('a', class_='name_item')
        ]
        item_urls = [f'{base_url}{href}' for href in item_hrefs]

        for url in item_urls:
            response = rs.get(url=url)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'lxml')

            name = soup.find('p', id='p_header').text
            article = soup.find('p', class_='article').text.lstrip('Артикул: ')
            count = soup.find('span', id='in_stock').text.lstrip('В наличии: ')
            price = soup.find('span', id='price').text
            old_price = soup.find('span', id='old_price').text

            lis = soup.find('ul', id='description').find_all('li')
            li_id = [li['id'] for li in lis]
            descriptions = [
                desc.text.split('\n') for desc in soup.find(
                    'ul', id='description'
                ).find_all('li')
            ]
            data = []
            for desc in descriptions:
                items = [item.split(':')[1].strip() for item in desc]
                data.append(items[0])
                description = dict(zip(li_id, data))

            result_json = []
            result_json.append({
                'categories': 'mobile',
                'name': name,
                'article': article,
                'description': description,
                'count': count,
                'price': price,
                'old_price': old_price,
                'link': url
            })

            with open('mobiles.json', 'a', encoding='utf-8') as file:
                json.dump(result_json, file, indent=4, ensure_ascii=False)
