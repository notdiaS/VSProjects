from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from lxml import etree 


url = "https://www.imdb.com/search/title/?title_type=feature&genres=!short,!documentary&user_rating=6,10&sort=user_rating,desc&num_votes=50000,"

HEADERS ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

response = requests.get(url,headers = HEADERS)

soap = BeautifulSoup(response.text,'html.parser')

box = soap.find('ul', class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-315eec58-0 hvFmRn detailed-list-view ipc-metadata-list--base") 

movieNames = box.find_all('h3', class_="ipc-title__text")

for movieName in movieNames:

 movieName = box.find('h3', class_="ipc-title__text").text
 print(movieName)
 

# movieNames = dom.xpath('//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[2]/ul/li[2]/div[1]/div/div/div[1]/div[2]/div[1]/a/h3')[0].text

