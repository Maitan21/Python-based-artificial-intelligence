from bs4 import BeautifulSoup

fp = open("lecture2/css-selector/fruits-vegetables.html",encoding="utf-8")
soup = BeautifulSoup(fp,"html.parser")

#Extract by CSS Selector
print(soup.select_one("li:nth-of-tpye(8)").string)
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)

#Extract by Find method
cond = {"data-lo":"us","class":"black"}
print(soup.find("li",cond).string)

#Extract by Find method continuable
print(soup.find(id="ve-list")
          .find("li",cond).string)