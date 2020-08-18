from bs4 import BeautifulSoup
import urllib.request as req
import datetime

#Bring HtML
url = "http://info.finance.naver.com/marketindex/"
res = req.urlopen(url)

#HTML Analysis
soup = BeautifulSoup(res, "html.parser")

#Extract Data
price = soup.select_one("div.head_info > span.value").string
print("usd/krw", price)

#Save data
t = datetime.date.today()
fname = t.strftime("%Y-%m-%d") + ".txt"
with open(fname, "w", encoding="utf-8") as f:
    f.write(price)