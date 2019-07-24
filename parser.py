## parser.py
import requests
from bs4 import BeautifulSoup

req = requests.get('https://work.mma.go.kr/caisBYIS/search/byjjecgeomsaekView.do?menu_id=m_m6&pageIndex=1&byjjeopche_cd=120171205&eopjong_gbcd=1&gegyumo_cd=&eopche_nm=&sido_addr=&sigungu_addr=&chaeyongym=&bjinwonym=&eopjong_gbcd_list=11111')
html = req.text
soup = BeautifulSoup(html, 'html.parser')

gots = soup.select('#content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2)')
for got in gots:
    a = int(got.text[0][0])
    print(a)

useds = soup.select('#content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)')
for used in useds:
    b = int(used.text[0][0])
    print(b)

res = a - b
print(res)