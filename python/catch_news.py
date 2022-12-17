import os
import re
import json
import time
import pandas as pd
from datetime import datetime
from selenium import webdriver
from bs4 import BeautifulSoup as Soup

timeStandard = 20
scrollTimes = 7

def packing(datas):
    select_df = pd.DataFrame(datas, columns = ['content', 'picture'])
    data = json.loads(select_df.to_json(orient = 'records'))

    if os.path.exists('python/news.json'):
        os.remove('python/news.json')
    
    with open('python/news.json', 'w', encoding='UTF-8') as f:
        json.dump(data, f, ensure_ascii= False)

def getDay(str):
    today = {
        "year": int(datetime.today().strftime('%Y')),
        "month": int(datetime.today().strftime('%m')),
        "day": int(datetime.today().strftime('%d'))
    } 
    timeTag = ["年", "月", "日"] 
    pos = [-1, -1, -1]
    for index in range(0, 3):
        if timeTag[index] in str: pos[index] = str.index(timeTag[index])
    month = int((str[:pos[1]])[pos[0] + 1:])
    day = int((str[pos[1] : pos[2]])[1:])
    distance = (today["month"] * 30 + today["day"]) - (month * 30 + day)
    return distance

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
    while(i < scrollTimes):
        js = 'window.scrollTo({top:document.body.scrollHeight , behavior: "smooth"})'
        browser.execute_script(js)
        i += 1
        time.sleep(1)
    time.sleep(5)

    soup = Soup(browser.page_source,"lxml")
    posters = soup.find_all("div", class_="x78zum5 x1n2onr6 xh8yej3")

    news = []
    for index, poster in enumerate(posters):
        tmp = []
        if index < 2 : continue
        date = poster.find("span", id=re.compile('^jsc_c_'))
        if date is not None:
            date = date.find("span", class_="x4k7w5x x1h91t0o x1h9r5lt xv2umb2 x1beo9mf xaigb6o x12ejxvf x3igimt xarpa2k xedcshv x1lytzrv x1t2pt76 x7ja8zs x1qrby5j x1jfb8zj")
            if date is not None:
                date.find("span")
                if date is not None:
                    if getDay(date.text) > timeStandard: break
        
        content = poster.select_one("div.x11i5rnm.xat24cr.x1mh8g0r.x1vvkbs.xdj266r")
        if content is not None:
            tmp.append(content.text)
        else: tmp.append("null")

        pictures = poster.select("img.x1ey2m1c.xds687c.x5yr21d.x10l6tqk.x17qophe.x13vifvy.xh8yej3")
        if pictures is not None:
            pict = []
            for picture in pictures:
                pict.append(picture.get("src"))
            tmp.append(pict)
        else: tmp.append("null")
        news.append(tmp)
    packing(news)
    print("Work Done")
        

