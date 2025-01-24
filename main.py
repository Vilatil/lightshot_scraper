import random
import re
import logging
import string
import time
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
URL="https://prnt.sc/"

def main():
    #logging.basicConfig(level=logging.INFO,filename="links.log")
    while True:
        time.sleep(1)
        proper_link = f'{URL}{create_a_link(5)}'
        get_a_link(proper_link)
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

def get_a_link(proper_link):

    response = requests.get(proper_link, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    picture = soup.find('img', class_='no-click screenshot-image')
    print(picture)
    light_shot_link = picture.get('src')
    print(f"{light_shot_link}")
    logging.info(f"{light_shot_link}")
    downloader(light_shot_link)

def downloader(light_shot_link):
    response = requests.get(light_shot_link, headers=headers)
    if response.status_code != 200:
        print(f"Failed to download image!{response.status_code}")
    filename = light_shot_link.split('/')[-1]
    with open(filename, 'wb') as img:
        img.write(response.content)
    print("Image downloaded successfully!")

if __name__ == "__main__":
    print(main())
