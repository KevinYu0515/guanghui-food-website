import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from handler import *
from logger import logger

timeStandard = 7
scrollTimes = 1
url = "https://www.facebook.com/profile.php?id=100075103166257"

if __name__ == '__main__':
    logger.info("Start Scraping")

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        service = Service("chromedriver.exe")
        browser = webdriver.Chrome(service=service, options=options)
        browser.set_page_load_timeout(10)
        browser.set_script_timeout(10)
        browser.maximize_window()
    except Exception as e:
        logger.error("Error initializing browser: %s", str(e))
        exit(1)

    try:
        browser.get(url)
        close_btn = browser.find_element("xpath", '//*[@aria-label="關閉"]')
        close_btn.click()
    except Exception as e:
        logger.error("Error closing pop-up: %s", str(e))
        browser.execute_script("window.stop()")

    time.sleep(3)

    try:
        i = 0
        while(i < scrollTimes):
            js = 'window.scrollTo({top:document.body.scrollHeight , behavior: "smooth"})'
            browser.execute_script(js)
            i += 1
            time.sleep(1)
    except Exception as e:
        logger.error("Error scrolling: %s", str(e))
        browser.execute_script("window.stop()")

    try:
        posts = browser.find_elements("xpath", '//*[@aria-posinset]')
        logger.info("Find %d posts", len(posts))
    except Exception as e:
        logger.error("Error finding posts: %s", str(e))
        browser.execute_script("window.stop()")
    
    time.sleep(3)
    
    news = []
    for index, post in enumerate(posts):
        try:
            logger.info("Processing post %d", index + 1)
            links = post.find_elements("xpath", './/a')
            for link in links:
                if "天" in link.text or "月" in link.text or "年" in link.text:
                    date = convert_date(link.text)
            
            content = post.find_element("xpath", './/*[contains(@data-ad-comet-preview, "message")]').text

            img = post.find_element("xpath", './/img').get_attribute("src")
            
            news.append({
                "date": date,
                "content": content,
                "picture": img,
            })
        except Exception as e:
            logger.error("Error processing post %d: %s", index + 1, str(e))
            browser.execute_script("window.stop()")

    packing(news)
    logger.info("Data packing completed")
        

