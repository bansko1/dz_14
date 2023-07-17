# Работа с beautifulsoup
# Парсер новостей сайта https://www.mos.ru

import requests
from bs4 import BeautifulSoup
import json

domain = 'https://www.mos.ru'
url = f'{domain}/news'

result = {}

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

tags_news = soup.find_all('a', class_='commonCard__link link-black')
for tag in tags_news:
    # print(tag.text)
    text = tag.text
    href = tag.get('href')
    # print(text, href)
    url = f'{domain}{href}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('p')
    # print(news)                                     # Проверка наличия новости в тегах
    text_list = []
    for part in news:
        # print(part.text)

        part_text = part.text.replace('\xa0', ' ')
        # print(part_text)
        text_list.append(part_text)
    # print(text_list)
    text_list = ' '.join(text_list)
    if text_list:
        result[text] = text_list
# print(result)
with open('result.json', 'w') as f:
    json.dump(result, f)
numb = result.items()
for i in range(len(result)):
    print('Новость', i)
    print('Заголовок: ', list(numb)[i][0])
    print('Текст: ', list(numb)[i][1])
