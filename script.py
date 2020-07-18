import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictWriter

base_url = 'http://quotes.toscrape.com/'


def scripe():
    url = '/page/1'
    quoted_list = []
    while url:
        req = requests.get(f'{base_url}{url}')
        soup = BeautifulSoup(req.text, 'html.parser')
        ele = soup.find_all(class_='quote')
        for q in ele:
            quoted_list.append({
                'text': q.find(class_='text').get_text(),
                'author': q.find(class_='author').get_text(),
                'link': q.find('a')['href']
            })
        next_btn = soup.find(class_='next')
        url = next_btn.find('a')['href'] if next_btn else None
    return quoted_list


def write_csv_file(f, q):
    with open(f, 'w')as file:
        hed = ['text', 'author', 'link']
        writer = DictWriter(file, fieldnames=hed)
        writer.writeheader()
        for qu in q:
            writer.writerow(qu)


quotes = scripe()
write_csv_file('sul.csv', quotes)
