import requests
import time
from bs4 import BeautifulSoup
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Chromium";v="154", "Google Chrome";v="154", "Not A(Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36',
}
Results=[]
pageno=2
for page in range(1,51):
       
    response = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html', headers=headers)
    if response.status_code!=200:
        time.sleep(0.5)
        response = requests.get(f'https://books.toscrape.com/catalogue/page-{page}.html', headers=headers)

    print('Page No', page,'--- Status Code',response.status_code)
    soup= BeautifulSoup(response.text, "html.parser")
    # Books=soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    Books=soup.find_all('article', class_='product_pod')

    for book in Books:
        
        title= book.find('h3').find('a')['title']
        book_link=book.find('h3').find('a')['href']
        price=book.find('p', class_="price_color").text
        instock_aval=book.find('p', class_="instock availability").text.strip()
        rating_element = soup.select_one("p.star-rating")
        rating=''

        if rating_element:
            rating_class = rating_element.get("class", [])
            rating = next(
                (cls for cls in rating_class if cls.lower() in
                ["one", "two", "three", "four", "five"]),
                None
            )
        data=   {
            'title':title,
            'link':book_link,
            'price': price,
            'instock_aval':instock_aval,
            'rating':rating,
            'page':page     
        } 
        Results.append(data)
import json
with open('Books.json','w',encoding='utf-8') as f:
    json.dump(Results,f,indent=4,ensure_ascii=False)
    



    

