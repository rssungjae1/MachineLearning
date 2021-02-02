from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import urllib.request

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def scrapping(key,num):
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element_by_name("q")
    elem.send_keys(key)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
    count = 1
    images_num = 0
    for image in images:
        images_num += 1
        if images_num > num:
            break
        try:
            if image.is_enabled():
                driver.execute_script("arguments[0].click();", image)
            else:
                time.sleep(5)
                driver.execute_script("arguments[0].click();", image)
            time.sleep(2)
            try:
                imgUrl = driver.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[2]/a/img').get_attribute("src")
            except NoSuchElementException as e:
                print(e)
                continue
            opener=urllib.request.build_opener()
            opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
            urllib.request.install_opener(opener)
            urllib.request.urlretrieve(imgUrl, "./img/" + key +  "/"+ str(count) + ".jpg")
            print("[생성완료] ./img/" + key +  "/"+ str(count) + ".jpg")
            count = count + 1
        except FileNotFoundError as err: 
            print(err)
        except:
            print("예상 외 에러 발생")
    driver.close()
    # 출력값
    return key