import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

from requests.models import ChunkedEncodingError, codes

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

coverSource = []
title = []
info = []
author = []
detailLink = []

url = 'http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf?orderClick=d79'

r = requests.get(url, headers=headers)

r.status_code

soupKyobo = BeautifulSoup(r.text, 'html.parser')

bestSellerUl = soupKyobo.find("ul", class_="list_type01")

while bestSellerUl.find("ul", class_="list_author") != None:
    bestSellerUl.find("ul", class_="list_author").replace_with('')

bestSellerLi = bestSellerUl.find_all("li")[0:8]

for li in bestSellerLi:
    coverSource.append(li.img["src"])
    title.append(li.find("div", class_="title").strong.text)
    detailLink.append(li.find("div", class_="cover").a["href"])
    info.append(li.find("div", class_="author").text)

for i in info:
    i = i.replace("\n", "")
    i = i.replace("\r", "")
    i = i.replace("\t", "")
    i = i.replace(" ", "")
    if(i.find("저자더보기") != -1):
        i = i.replace("저자더보기", " 외")
    index = i.find('|')
    i = i[0:index]
    author.append(i)

bookInfo = [[], [], [], [], [], [], [], []]
for i in range(8):
    bookInfo[i].append(str(i+1))
    bookInfo[i].append(coverSource[i])
    bookInfo[i].append(title[i])
    bookInfo[i].append(author[i])
