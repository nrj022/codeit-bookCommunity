import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = f'https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we'
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

book = soup.select('.ss_book_box')
title = []
author = []
cover = []

cnt = 0
for i in book:
    cnt += 1
    if cnt <= 8:    # 베스트셀러 8위까지
        title.append(i.select_one('.bo3').b.text)
        author.append(i.select_one(
            '.bo3').parent.next_sibling.next_sibling.a.string)

        try:
            cover.append(i.select_one('.i_cover')['src'])
        except TypeError:
            cover.append('')
        # with urlopen(imgUrl) as c:
        #     with open('aladin_' + str(cnt) + '.jpg', 'wb') as h:
        #         img = c.read()
        #         h.write(img)

# f = open(f'aladin.csv', 'w', encoding='utf-8', newline='')
# csvWriter = csv.writer(f)
# for i in bookList:
#     csvWriter.writerow(i)
# f.close()
