import requests
from bs4 import BeautifulSoup
from random import choice
from csv import DictReader
base_url = 'http://quotes.toscrape.com/'


def reader(filename):
    with open(filename) as file:
        return list(DictReader(file))


def start_game(quotes):
    rquote = choice(quotes)
    author = rquote['author']
    text = rquote['text']
    link = rquote['link']
    print(text)
    number_of_guess = 4
    guess = ''
    while guess != author and number_of_guess > 0:
        guess = input(
            f'who said this quote, remaining gusses {number_of_guess}.: \n')
        if guess == author:
            print('Good!! you got it')
            break

        number_of_guess -= 1
        if number_of_guess == 3:
            req = requests.get(f'{base_url}{link}')
            so = BeautifulSoup(req.text, 'html.parser')
            date = so.find(class_='author-born-date').get_text()
            loc = so.find(class_='author-born-location').get_text()
            print(f' Here is a hint author was born on {date} {loc}')
        elif number_of_guess == 2:
            init = author[0]
            print(f'author first initial {init}')

        elif number_of_guess == 1:
            ini = author.split()[1][0]
            print(f'author last initial {ini}')
        else:
            print(f'sorry you ran out of gusses the answer is {author}')

    agn = ' '
    while agn not in ('y', 'n'):
        agn = input('do you wana play again y/n : ')
        if agn == 'y':
            return start_game(q)
        else:
            print("OK GOOD BYE!!!")


q = reader('sul.csv')
start_game(q)
