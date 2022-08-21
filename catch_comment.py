from asyncio import ensure_future
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

    browser = webdriver.Edge()
    url = "https://reurl.cc/KQ0xNj"
    browser.set_page_load_timeout(10)
    browser.set_script_timeout(10)

    try:
        browser.get(url)
    except:
        browser.execute_script("window.stop()")

    browser.maximize_window()

    data_index = 4 
    sort_index = 2
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
    js = 'document.getElementsByClassName("m6QErb DxyBCb kA9KIf dS8AEf")[0].scrollTop=1000000'
    browser.execute_script(js)

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
        obj.append(ar.find(class_ = "rsqaWe").text)
        obj.append(ar.find(class_ = "wiI7pd").text)
        comments.append(obj)
    
    # dict = {"name":name,
    #         "star":star_review,
    #         "date":date_review,
    #         "text":text_review
    #         }
    # print(comments)
    select_df = pd.DataFrame(comments, columns = ['id','name','star','date','content'])
    data = json.loads(select_df.to_json(orient = 'records'))
    j = {"comments": data }
    with open('comment.json', 'w', encoding='UTF-8') as f:
        json.dump(j, f, ensure_ascii= False)
    # # select_df.to_excel('data_sample.xlsx')
