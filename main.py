import requests
from bs4 import BeautifulSoup
us1= 'https://mobizil.com/mobiles/oppo'
headers={"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
s=requests.Session()
r=s.get(us1)
soup=BeautifulSoup(r.content,"lxml")
print(soup.text)
for x in soup.findAll('ddiv',{'class':'aps-content'}):
    for title in x('div',{'class':'aps-product-box'}):
        for href in title('a'):
            print(href.text)
