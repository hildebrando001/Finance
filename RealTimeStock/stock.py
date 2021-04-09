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
            price, change = [], []



        texts = web_content_div(web_content, 'D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)')
        if texts != []:
            for  count, vol in enumerate(texts):
                if vol == 'Volume':
                    volume = texts[count + 1]
        else:
            volume = []

        pattern = web_content_div(web_content, 'Fz(xs) Mb(ppx)')
        try: # Trying if it is sending information inside this pattern
            latest_pattern = pattern[0]
        except IndexError:
            latest_pattern = []

        texts = web_content_div(web_content, 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)')
        if texts != []:
            for count, target in enumerate(texts):
                if target == '1y Target Est':
                    one_year_target =  texts[count + 1]
        else:
            one_year_target = []




    except ConnectionError: # In case of a connection error when trying to get the content
        price, change, volume, latest_pattern, one_year_target = [], [], [], [], [] # In case of there is no content

    return price, change, volume, latest_pattern, one_year_target


print(real_time_price(Stock[0]))
print(real_time_price(Stock[1]))
