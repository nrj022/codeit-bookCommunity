import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from requests.models import ChunkedEncodingError, codes

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

coverSource = []
title = []
author = []

url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'

r = requests.get(url, headers=headers)

r.status_code

soupKyobo = BeautifulSoup(r.text, 'html.parser')

bestSellerUl = soupKyobo.find("ul", class_="list_type01")

while bestSellerUl.find("ul", class_="list_author") != None:
    bestSellerUl.find("ul", class_="list_author").replace_with('')

bestSellerLi = bestSellerUl.find_all("li")[0:8]

for  li in bestSellerLi:
    coverSource.append(li.img["src"])
    title.append(li.find("div", class_="title").strong.text)
    """ authorDiv = li.find("div", class_="author")
    while authorDiv.find("span") != None:
        authorDiv.find("span").replace_with('') """
    """ print(li.text) """

''' with open("sampleHtml.html", "r+") as f:
    data = f.read()
    soupHomePage = BeautifulSoup(data, "html.parser")
    li = soupHomePage.select_one("li")
    print(li)
    content = '<a href="#">Link</a>'
    li.append(BeautifulSoup(content, 'html.parser'))
    print(li)
    print(soupHomePage) '''




''' with open("sampleHtml.html", "w", encoding="utf8") as file:
    file.write() '''