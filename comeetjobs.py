import requests

cookies = {
    'visid_incap_2167377': 'me8+pERNQVSR+TE388H0FKfwzWoAAAAAQUIPAAAAAAAadIsENHSnE3QH0KE+hOGz',
    'nlbi_2167377': 'ljX5e/rLYUxn15sZl+tn0AAAAABYlibGusjIJpxcELY1+7Fh',
    'incap_ses_667_2167377': '/uQhVHwoGyJX8QbOZKlBCanwzWoAAAAAQKGd/dUXpDR6vBR0pFm9uw==',
    'incap_ses_937_2167377': 'tMwidFc1bh04lNGn4eQADa3wzWoAAAAAjCncA7dd0o1Fd6I7JYNNSQ==',
    'referrer98_008': 'https%3A%2F%2Fwww.google.com%2F',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
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
    # 'cookie': 'visid_incap_2167377=me8+pERNQVSR+TE388H0FKfwzWoAAAAAQUIPAAAAAAAadIsENHSnE3QH0KE+hOGz; nlbi_2167377=ljX5e/rLYUxn15sZl+tn0AAAAABYlibGusjIJpxcELY1+7Fh; incap_ses_667_2167377=/uQhVHwoGyJX8QbOZKlBCanwzWoAAAAAQKGd/dUXpDR6vBR0pFm9uw==; incap_ses_937_2167377=tMwidFc1bh04lNGn4eQADa3wzWoAAAAAjCncA7dd0o1Fd6I7JYNNSQ==; referrer98_008=https%3A%2F%2Fwww.google.com%2F',
}

response = requests.get('https://www.comeet.com/jobs/tripleten/98.008', cookies=cookies, headers=headers)
JSONStr=response.text.split("COMPANY_POSITIONS_DATA =")[1].split('];')[0]+']'
print(JSONStr)
import json
data=json.loads(JSONStr)
print(len(data))
with open('ComeetJobs.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)