import requests
from bs4 import BeautifulSoup

cookies = {
    '_gcl_au': '1.1.1522627199.1792587408',
    '_ga': 'GA1.2.522677848.1792587408',
    '_gid': 'GA1.2.636897884.1792587408',
    '_fbp': 'fb.1.1792587408008.35007266541566513',
    '_ga_09N5RQCFG4': 'GS2.2.s1792587408$o1$g0$t1792587408$j60$l0$h0',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/jxl,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'referer': 'https://www.google.com/',
    'sec-ch-ua': '"Google Chrome";v="155", "Chromium";v="155", "Not(A:Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/155.0.0.0 Safari/537.36',
    # 'cookie': '_gcl_au=1.1.1522627199.1792587408; _ga=GA1.2.522677848.1792587408; _gid=GA1.2.636897884.1792587408; _fbp=fb.1.1792587408008.35007266541566513; _ga_09N5RQCFG4=GS2.2.s1792587408$o1$g0$t1792587408$j60$l0$h0',
}

response = requests.get('https://www.scrapethissite.com/pages/', cookies=cookies, headers=headers)

soup= BeautifulSoup(response.text,'html.parser')
pages=soup.find_all("div", class_='page')


for page in pages:
    desc=page.find('p', class_='lead session-desc')
    print(desc)