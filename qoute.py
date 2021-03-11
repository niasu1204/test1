import os, re, usecsv
import urllib.request as ur
#urllib : 웹에서 얻은 데이터를 다루는 패키지
#request : 웹 문서를 열어 데이터를 읽어오는 모듈
from bs4 import BeautifulSoup as bs

url = 'http://quotes.toscrape.com/'
html = ur.urlopen(url)

#print(html.read()[:100])
soup = bs(html.read(), 'html.parser')
#print(soup)
#print(type(html))
#print(type(soup))

#print(soup.find_all('span')[0].text)

for i in soup.find_all('span'):
    print(i.text)

for i in soup.find_all('span',{"class":"text"}):
    print(i.text)