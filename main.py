import random
import logging
import string
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

URL="https://prnt.sc/"

def main():
    #logging.basicConfig(level=logging.INFO,filename="links.log")
    while True:
        time.sleep(1)
        proper_link = f'{URL}{create_a_link(5)}'
        download_a_photo(proper_link)
    return

def create_a_link(k):
    link=""
    while k >= 0:
        letter_or_number = random.randint(0,1)
        if (letter_or_number == 0):
           number = random.choice(string.digits)
           link+=number
        else:
            letter = random.choice(string.ascii_lowercase)
            link+=letter
        k-=1
    return link

def download_a_photo(proper_link):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(proper_link, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    picture = soup.find('img', class_='no-click screenshot-image')
    print(picture)
    light_shot_link = picture.get('src')
    print(f"{light_shot_link}")
    logging.info(f"{light_shot_link}")
    if "imgur" in light_shot_link:
        print(imgur_link(light_shot_link))
    else:
        print("nevazhno")
def imgur_link(light_shot_link):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(light_shot_link, headers=headers)
    if response.status_code == 200:
        options = Options()
        options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36") 
        driver = webdriver.Chrome(options=options) 
        driver.get(light_shot_link)
        picture = WebDriverWait(driver,4).until(
            EC.presence_of_element_located((By.XPATH, '//img[contains(@class,"image-placeholder")]'))
        )
        ready_picture = picture.get_attribute("src")
        print(ready_picture)
        if ready_picture:
            print(ready_picture)
        driver.quit()

print(main())


