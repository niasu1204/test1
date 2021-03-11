import os, re, usecsv
import urllib.request as ur
from bs4 import BeautifulSoup as bs


url= 'https://news.daum.net'
soup = bs(ur.urlopen(url).read(),'html.parser')

f= open('article.txt','w', encoding='utf-8')
for i in soup.find_all('div', {"class":"item_issue"}):
    try:
        f.write(i.text+'\n')
        f.write(i.find_all('a')[0].get("href")+'\n')
        soup2 = bs(ur.urlopen(i.find_all('a')[0].get("href")).read(),'html.parser')
        for j in soup2.find_all('div',{"class":"news_view"}):
            f.write(j.text)
    except:
        pass        

f.close()


# for i in soup.find_all('div', {"class":"item_issue"}):
#     print(i.text)

# a = soup.find_all('a')[:5]
# for i in a:
#     print(i.get("href"))

# url2 ='https://news.v.daum.net/v/20210307144659421'
# soup2 = bs(ur.urlopen(url2).read(),'html.parser')

