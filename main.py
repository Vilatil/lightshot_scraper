import random
from datetime import datetime
import os
import re
import logging
import string
import time
import requests
from bs4 import BeautifulSoup
import mysql.connector
from mydb import make_entry, mycursor

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

URL = "https://prnt.sc/"

def main():
    logging.basicConfig(level=logging.INFO)
    create_a_folder()
    while True:
        created_link = URL + create_a_link(5)
        logging.info(f"the created link: {created_link}")
        get_src(created_link)
    return

def create_a_folder():
    folder = './images' 
    if not os.path.exists(folder):
        os.makedirs(folder)

def create_a_link(k):
    characters = string.ascii_lowercase + string.digits
    link = ''.join(random.choices(characters, k=k))
    return link

def get_src(created_link):
    response = requests.get(created_link, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    picture = soup.find('img', class_='no-click screenshot-image')
    if not picture:
        logging.warning("picture not found, gonna try another link")
        return
    light_shot_link = picture.get('src')
    if "0_173a7b_211be8ff.png" in light_shot_link:
        logging.info("the photo was removed from the website")
        return
    logging.info(f"the link for downloading: {light_shot_link}")
    downloader(light_shot_link)

def downloader(light_shot_link):
    if not light_shot_link.startswith("https:"):
        light_shot_link = "https:" + light_shot_link
    response = requests.get(light_shot_link, headers=headers)
    if response.status_code != 200:
        logging.error(f"Failed to download image! ERROR:{response.status_code}")
        return
    filename = light_shot_link.split('/')[-1]
    make_entry(mycursor,filename)
    with open(f'./images/{filename}', 'wb') as img:
        img.write(response.content)
    logging.info("Image was successfully downloaded!")

if __name__ == "__main__":
    main()
