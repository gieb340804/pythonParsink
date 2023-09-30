import requests
import time
from datetime import date 
import re

from bs4 import BeautifulSoup as b

import telebot


URL = 'https://27trk.ru/news/'
API_KEY = '6689325491:AAHPd2yGl_w78sE3zUCZjOrSOsfR6mkaWqg'
bot = telebot.TeleBot(API_KEY )
chat_id=-1001971945044

# нахождение настоящей даты для сравнения
today = date.today().strftime('%d.%m.%Y')
print(today)


""" r = requests.get(URL)
soup = b(r.text, 'html.parser')
news = soup.find_all('a', class_='title-link')
# news = soup.find('a', class_='title-link')
news_text = [c.text for c in news]
print(news_text)
 """


r = requests.get(URL)
soup = b(r.text, 'html.parser')

news = soup.find_all('div', class_='col-picture col-sm-6')
for a in news:
    #находит дату в новостях
    day = soup.find('div', class_='date-block')
    # print(day.text.strip())
    date_text = day.text.strip()
    date_match = re.search(r'\b\d{2}\.\d{2}\.\d{4}\b', date_text)
    if date_match:
        date = date_match.group()  # Получаем совпадение регулярного выражения
        print(date)
        """ В этом примере мы используем модуль `re` и функцию `re.search()` для поиска подстроки, 
        соответствующей паттерну регулярного выражения `r'\b\d{2}\.\d{2}\.\d{4}\b'`. Паттерн `\b\d{2}\.\d{2}\.\d{4}\b` соответствует дате в формате "dd.mm.yyyy". 
        vЕсли совпадение найдено, мы извлекаем его с помощью метода `.group()` и выводим результат. """

    # print(a.find('a')['href']
    aHref = a.find('a')['href']
    URLA = 'https://27trk.ru' + aHref
    print(URLA)
    ra = requests.get(URLA)
    soups = b(ra.text, 'html.parser')
    newsa = soups.find("h1")
    print(newsa)


# news_text = [c.text for c in news]
# print(news_text)








async def st():
    
    while True: 
        bot.send_message(chat_id, news_text)
        time.sleep(25)
        
st()


