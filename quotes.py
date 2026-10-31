import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://quotes.toscrape.com/page/2/',
    'sec-ch-ua': '"Chromium";v="154", "Google Chrome";v="154", "Not A(Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36',
}

result=[]
page=1
while True:
    response = requests.get(f'https://quotes.toscrape.com/page/{page}/', headers=headers)
    print("Status ", response.status_code,"------page ", page)
    soup= BeautifulSoup(response.text,'html.parser')
    quotes=soup.find_all("div", class_='quote')
    if len(quotes)==0:
        print("no of pages= ", page)
        break


    for quote in quotes:
        
        quotetext=quote.find('span',class_='text').text
        author=quote.find('small',class_='author').text 
        tags=quote.find_all('a',class_='tag')
        tagtext=[]
        for tag in tags:
            tagtext.append(tag.text )
        TagsActual=', '.join(tagtext)    
        data={
            'Qoute':quotetext,
            'author':author,
            'tags':TagsActual,
            'Page No':page
        }
        result.append(data)
        # print(data)
    page+=1
        
import json
with open('quotes.json','w',encoding='utf-8') as f:
    json.dump(result,f,indent=4,ensure_ascii=False)