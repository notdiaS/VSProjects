import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium.webdriver.support.wait import WebDriverWait
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from lxml import html


y = 126
site = 'https://www.epey.com/laptop/e/YToyOntpOjEzNjA7YToxOntpOjA7czo2OiIxMDU2MTkiO31pOjE0OTM7YToxOntpOjA7czo2OiIxMTc5MTQiO319X2I6MDs=/{}'.format(y)

path = 'D:\ChromeDriver\chrome-win64'


driver = uc.Chrome()




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.110 Safari/537.36'
}

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

next = ''

i = 127
retNum = 15
x = 0
csv_file_path = 'laptop-data-lastv3-10.csv'

data_list = []

while x < retNum:

 req = session.get((site),headers=headers)
 print(site)

 content = req.text

 result = BeautifulSoup(content, 'html.parser')

 productTable = result.find('div', class_='listele table')

 productLinks = productTable.find_all('ul',class_='metin row')



 for productLink in productLinks[1:]:
  
        link = productLink.find('a')['href']
        print(link)
        linkToCopy = str(productLink.find('a')['href'])
        

        #  print(link)
        

            
        reqLink = requests.get(link,headers=headers)

        cont = reqLink.text

        res = BeautifulSoup(cont, 'html.parser')

        info = res.find('div', id="bilgiler")
        
        driver.get(link)
        
        
        try:
             
            #SCORE 
            '' 
            score = driver.find_element(by=By.XPATH, value="(//span[@class='circle-text'])[1]")
            print(score.text)
            scoreToCopy = score.text
                
            
            
            ## SCREEN

            screen = info.find('li',id='id1426').find('a').text 
            print(screen)
            screenRes = info.find('li',id='id1036').find('a').text
            print(screenRes)
            screenRefRate = info.find('li',id='id6294').find('a').text
            print(screenRefRate)
        
            


            ## CPU
            cpuModel = info.find('li',id='id1364').find('a').text
            print(cpuModel)
            cpuFreq = info.find('li',id='id1375').find('a').text
            print(cpuFreq)
            cpuCore = info.find('li',id='id1373').find('a').text
            print(cpuCore)
            cpuICore = driver.find_element(by=By.XPATH,value='//*[@id="id1374"]/span/span').text
            print(cpuICore)
            cpuCache = info.find('li',id='id1372').find('a').text
            print(cpuCache)
            cpuTranDist = info.find('li',id='id1398').find('a').text
            print(cpuTranDist)

            ## RAM
            ramMemory = info.find('li',id='id1027').find('a').text
            print(ramMemory)


            ## STORAGE
            ssdSize = info.find('li',id='id1422').find('a').text
            print(ssdSize)
            
            ## GPU
            gpuModel = info.find('li',id='id1399').find('a').text
            print(gpuModel)
            gpuVram = info.find('li',id='id1410').find('a').text
            print(gpuVram)
            gpuFreq = driver.find_element(by=By.XPATH,value='//*[@id="id1403"]/span/span').text
            print(gpuFreq)
            gpuMFreq = driver.find_element(by=By.XPATH,value='//*[@id="id1404"]/span/span').text
            print(gpuMFreq)

            data_list.append([linkToCopy, scoreToCopy, screen, screenRes, screenRefRate, cpuModel, cpuFreq, cpuCore, cpuICore,
                            cpuCache, cpuTranDist, ramMemory, ssdSize, gpuModel, gpuVram, gpuFreq, gpuMFreq])

        except:
         pass
        
        
  
 next = '{}/'.format(i) 
 site = 'https://www.epey.com/laptop/e/YToxOntzOjQ6Im96ZWwiO2E6MTp7aTowO3M6Nzoic2F0aXN0YSI7fX1fTjs=/{}'.format(next)
 i +=1
 x +=1


driver.quit()
   



# Writing to CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write header
    writer.writerow(["Link", "Score","Screen", "Screen Resolution", "Screen Refresh Rate",
                     "CPU Model", "CPU Frequency", "CPU Cores", "CPU Integrated Cores", "CPU Cache",
                     "CPU Transfer Distance", "RAM Memory", "SSD Size", "GPU Model", "GPU VRAM",
                     "GPU Frequency", "GPU Memory Frequency"])
    # Write data
    for row in data_list:
        writer.writerow(row)

print(f"Data has been saved to {csv_file_path}")   

 
    



    
