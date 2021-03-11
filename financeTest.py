from bs4 import BeautifulSoup
from datetime import datetime
# pip install requests 
import requests
import time

#https://finance.naver.com
#https://finance.naver.com/item/main.nhn?code=company_code

def get_code(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    bs_obj = get_code(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    now_price = blind.text
    return now_price

company_codes = ["005930","024810","000660"] 

# now_price = get_price("000660")
# print("now_price : ",now_price)

# for item in company_codes:
#         now_price = get_price(item)
#         print(now_price)
#         print("-------------------------------")

while True:
    print("test")

    now = datetime.now()
    print(now)
    
    for item in company_codes:
        now_price = get_price(item)
        print(now_price)
    print("-------------------------------")
    time.sleep(60)
