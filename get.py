#!/bin/python3
from bs4 import BeautifulSoup
import requests as r
import sys
import os

url = sys.argv[1]
html = r.get(url).text
soup = BeautifulSoup(html, 'html.parser')

title = soup.title.text
img_urls = soup.find_all("img")
img_urls = [each['src'] for each in img_urls if not each['src'].startswith("data:")]
print(img_urls)

print(title)

if os.path.exists(title):
    i = 0
    while os.path.exists(title + str(i)):
        i += 1
    dir = title + str(i)
else:
    dir = title
os.mkdir(dir)

for index in range(len(img_urls)):
    try:
        with open(f"{dir}/{index}.jpg", 'wb') as f:
            img = r.get(img_urls[index]).content
            f.write(img)
    except r.exceptions.InvalidSchema:
        print(f"第{index}个url为{url}的图片抛出InvalidSchema异常")



        
#for each in img_urls:
    #os.system("firefox " + each)
    
