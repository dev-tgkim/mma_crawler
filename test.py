from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver')
driver.get('https://work.mma.go.kr/caisBYIS/search/byjjecgeomsaek.do')
# 페이지 접속
driver.find_element_by_name('eopjong_gbcd').click()
driver.find_element_by_css_selector('#eopjong_gbcd > option:nth-child(2)').click()
# 산업기능요원 선택
driver.find_element_by_id('eopjong_cd13').click()
# 정보처리 선택
driver.find_element_by_css_selector('#content > form > p > span.btn.icon_search > a').click()
# 조회 클릭

time.sleep(2)
res = 0


print(driver.find_element_by_css_selector('#content > div.page_move_n > a:nth-child(12)').text)

# for index in range(10):
#     link = driver.find_element_by_css_selector('#content > table > tbody > tr:nth-child(' + str(index + 1) + ') > th > a')
#     link.click()
#     time.sleep(1)

#     gots = driver.find_element_by_css_selector('#content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2)')
#     for got in gots:
#         a = int(got.text[0][0])
#         print(a)

#     useds = driver.find_element_by_css_selector('#content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)')
#     for used in useds:
#         b = int(used.text[0][0])
#         print(b)

#     temp = a - b
#     res = res + temp

#     driver.back()
#     time.sleep(1)