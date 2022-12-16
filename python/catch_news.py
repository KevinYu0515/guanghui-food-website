import os
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import time

if __name__ == '__main__':
    
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument('-disable-gpu')
    edge_options.add_argument('log-level=3')
    browser = webdriver.Edge("python/msedgedriver.exe", options=edge_options)
    url = "http://gg.gg/guanghui-facebook-wuqui"
    browser.set_page_load_timeout(10)
    browser.set_script_timeout(10)
    browser.maximize_window()

    try:
        browser.get(url)
    except:
        browser.execute_script("window.stop()")

    time.sleep(3)

    i = 0
    while(i < 7):
        js = 'window.scrollTo({top:document.body.scrollHeight , behavior: "smooth"})'
        browser.execute_script(js)
        i += 1
        time.sleep(1)
    time.sleep(5)

    soup = Soup(browser.page_source,"lxml")
    dates = soup.find_all("span", id=re.compile('^jsc_c_'))
    for index in range(0 ,len(dates)):
        date = dates[index].find("span", class_="x4k7w5x x1h91t0o x1h9r5lt xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j x1jfb8zj")
        tt = date.find("span")
        if tt is not None:
            print(tt.text)