import pandas as pd
import datetime
import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup

Stock = ['BRK-B', 'PETR4.SA']

class_path = 'My(6px) Pos(r) smartphone_Mt(6px)'


def web_content_div(web_content, class_path):
    web_content_div = web_content.find_all('div', {'class':class_path}) # search all the div with this class
    try:
        spans = web_content_div[0].find_all('span') # find all the span inside the div
        texts = [span.get_text() for span in spans] # create a list with content of the spans
    except IndexError:
        texts = []
    return texts


def real_time_price(stock_code):
    url = 'https://finance.yahoo.com/quote/' + stock_code + '?p=' + stock_code + '&.tsrc=fin-srch'
    try:
        r = requests.get(url)
        web_content = BeautifulSoup(r.text, 'lxml')
        texts = web_content_div(web_content, 'My(6px) Pos(r) smartphone_Mt(6px)')
        if texts != []:
            price, change = texts[0], texts[1] # [0] = price, [1] = rice changes
        else:
            print('tá caindo no else')
            price, change = [], []
    except ConnectionError: # In case of a connection error when trying to get the content
        price, change = [], [] # In case of there is no content
        print("tá caindo no except")

    return price, change


print(real_time_price(Stock[0]))
print(real_time_price(Stock[1]))
