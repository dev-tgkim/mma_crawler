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
totalgot = 0
totalused = 0
res = 0

pageIndex = 1

while pageIndex < 11:
    
    for index in range(10):
        link = driver.find_element_by_css_selector('#content > table > tbody > tr:nth-child(' + str(index + 1) + ') > th > a')
        link.click()
        time.sleep(1)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        gots = soup.select('#content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2)')
        for got in gots:
            a = int(got.text[0][0])
            print(a)

        useds = soup.select('#content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)')
        for used in useds:
            b = int(used.text[0][0])
            print(b)

        print('.')
        temp = a - b
        totalgot = totalgot + a
        totalused = totalused + b
        res = res + temp

        driver.back()
        time.sleep(1)

    time.sleep(3)

    if driver.find_element_by_css_selector('#content > div.page_move_n > a:nth-child(' + str(pageIndex + 3) + ')').text != '59':
        driver.find_element_by_css_selector('#content > div.page_move_n > a:nth-child(' + str(pageIndex + 3) + ')').click()

        if pageIndex == 10:
            pageIndex = 1
            print('new page')
        
    elif driver.find_element_by_css_selector('#content > div.page_move_n > a:nth-child(' + str(pageIndex + 3) + ')').text == '59':
        driver.find_element_by_css_selector('#content > div.page_move_n > a:nth-child(' + str(pageIndex + 3) + ')').click()

        for index in range(10):
            link = driver.find_element_by_css_selector('#content > table > tbody > tr:nth-child(' + str(index + 1) + ') > th > a')
            link.click()
            time.sleep(1)

            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')

            gots = soup.select('#content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(2)')
            for got in gots:
                a = int(got.text[0][0])
                print(a)

            useds = soup.select('#content > div:nth-child(2) > table > tbody > tr:nth-child(4) > td:nth-child(2)')
            for used in useds:
                b = int(used.text[0][0])
                print(b)

            print('.')
            temp = a - b
            totalgot = totalgot + a
            totalused = totalused + b
            res = res + temp

            driver.back()
            time.sleep(1)
        
        break

    pageIndex = pageIndex + 1
        

#########


print('total got : ' + str(totalgot))
print('total used : ' + str(totalused))
print(res)