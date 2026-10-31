import requests
from bs4 import BeautifulSoup
with open("sample.html") as f:
    html_doc=f.read()

soup=BeautifulSoup(html_doc, 'html.parser') 
# print(soup.title.text , type(soup))

print(soup.find(class_="div3"))