import requests
from bs4 import BeautifulSoup


def read_price(stock_code):
    url = ('http://finance.yahoo.com/quote/') + stock_code + ('.HK?p=') + stock_code + ('.HK&.tsrc=fin-srch')
    r = requests.get(url)
    web_content = BeautifulSoup(r.text, 'lxml')
    web_content = web_content.find("span",{"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    web_content = web_content.text
    return web_content

web_content = read_price('0001')
print(web_content)
