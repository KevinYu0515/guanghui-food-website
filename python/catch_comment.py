import os
import re
import time
import json
import pandas as pd
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup as Soup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':

    browser = webdriver.Edge("python\msedgedriver.exe")
    url = "https://reurl.cc/KQ0xNj"
    browser.set_page_load_timeout(10)
    browser.set_script_timeout(10)

    try:
        browser.get(url)
    except:
        browser.execute_script("window.stop()")

    browser.maximize_window()

    data_index = 4 
    sort_index = 1
    WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.CLASS_NAME, 'S9kvJb')))
    category_click = browser.find_elements(By.CLASS_NAME,'S9kvJb')
    print(category_click[data_index].text, "pass")
    time.sleep(1)
    category_click[data_index].click()
    time.sleep(1)
    category_click = browser.find_elements(By.CLASS_NAME,'fxNQSd')
    print(category_click[sort_index].text, "pass")
    time.sleep(1)
    category_click[sort_index].click()

    time.sleep(1)
    js ='document.getElementsByClassName("m6QErb DxyBCb kA9KIf dS8AEf")[0].scrollTop=100000000'
    for t in range(1, 5):
        browser.execute_script(js)
        time.sleep(1)

    time.sleep(1)
    buttons = browser.find_elements(By.CLASS_NAME,'w8nwRe')
    for button in buttons:
        button.click()

    
    time.sleep(3)
    soup = Soup(browser.page_source,"lxml")
    all_reviews = soup.find_all(class_ = 'jftiEf fontBodyMedium')

    comments = []
    i = -1
    for ar in all_reviews:
        i += 1
        obj = []
        obj.append(i)
        obj.append(ar.find(class_ = "d4r55").text)
        obj.append(str(ar.find(class_ = "kvMYJc").get('aria-label').strip().strip(" 顆星")))
        if int(obj[2]) < 4 : continue
        obj.append(ar.find(class_ = "rsqaWe").text)
        obj.append(ar.find(class_ = "wiI7pd").text)
        if len(obj[4]) < 5 : continue
        obj.append(ar.find(class_ = "NBa7we").get('src'))
        comments.append(obj)
    select_df = pd.DataFrame(comments, columns = ['id','name','star','date','content','icon'])
    data = json.loads(select_df.to_json(orient = 'records'))

    if os.path.exists('python\comment.json'):
        os.remove('python\comment.json')
    
    with open('python\comment.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii= False)
