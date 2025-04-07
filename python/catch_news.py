import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from handler import *
from logger import logger

timeStandard = 7
scrollTimes = 1
url = "https://www.facebook.com/profile.php?id=100075103166257"

if __name__ == '__main__':
    logger.info("Start Scraping")
    debug = os.environ.get("DEBUG", 0)
    limit = os.environ.get("LIMIT", 7)

    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-gpu')
        options.add_argument('--log-level=3')
        options.add_argument('--lang=zh-TW')

        if(os.environ.get("SELENIUM_REMOTE_URL") is not None):
            logger.info("Using Selenium Remote URL: %s", os.environ.get("SELENIUM_REMOTE_URL"))
            selenium_url = os.environ.get("SELENIUM_REMOTE_URL")
            browser = webdriver.Remote(
                command_executor=selenium_url,
                options=options
            )
        else:
            logger.info("Using local Chrome driver")
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
        close_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@aria-label="關閉"]'))
        )
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
            time.sleep(5)
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

    if debug:
        with open('debug.html', 'w', encoding='utf-8') as f:
            f.write(browser.page_source)
    
    news = []
    for index, post in enumerate(posts):
        try:
            logger.info("Processing post %d", index + 1)
            links = WebDriverWait(post, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'a')))
            for link in links:
                if "天" in link.text or "月" in link.text or "年" in link.text:
                    date = convert_date(link.text)
            if invalid_date(date, limit):
                continue

            logger.info("Post %d｜Date: %s", index, date)
            content = post.find_element("xpath", './/*[contains(@data-ad-comet-preview, "message")]').text
            logger.info("Post %d｜Content: %s", index, content)
            img = post.find_element("xpath", './/img').get_attribute("src")
            logger.info("Post %d｜Image: %s", index, img)
            news.append({
                "date": date,
                "content": content,
                "picture": img,
            })
        except Exception as e:
            logger.error("Error processing post %d: %s", index + 1, str(e))
            browser.execute_script("window.stop()")
    logger.info("There are %d posts", len(news))
    use_firebase(news)
    logger.info("Data packing completed")
        

