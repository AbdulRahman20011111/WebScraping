import requests
import json
from bs4 import BeautifulSoup
import time


headers = {
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/json',
    'origin': 'https://workday.wd5.myworkdayjobs.com',
    'priority': 'u=1, i',
    'referer': 'https://workday.wd5.myworkdayjobs.com/Workday',
    'sec-ch-ua': '"Chromium";v="154", "Google Chrome";v="154", "Not A(Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36',
    'x-calypso-csrf-token': '99c7b02d-1fb0-4d77-a6e8-9e8de4a76082',
    # 'cookie': 'PLAY_SESSION=81a028687878cc044c5cf5fdb268019fb0293fe7-workday_pSessionId=fd0shepeflient7i5fdgevofh2&instance=vps-prod-xw758zye.prod-vps.pr501.cust.pdx.wd; wd-browser-id=214bea74-6df2-4116-abdf-6fc512afd079; CALYPSO_CSRF_TOKEN=99c7b02d-1fb0-4d77-a6e8-9e8de4a76082; CALYPSO_SESSION=85f2c930-4f4f-42b2-a2b3-9cd3efb49bf7.d29ya2RheQ==.V0RDQzEuMIQAJQAAIJ/LyzvV2F/AbEOeXaeOdz/vWMFqO2KSFlHPac2e6scsAACMABYBMQAQ+llfZJUoMze4pgDm8ga9hAAAADg1ZjJjOTMwLTRmNGYtNDJiMi1hMmIzLTljZDNlZmI0OWJmNw==; wday_vps_cookie=669686794.53810.0000; __cflb=02DiuHJZe28xXz6hQKLf1exjNbMDM5uxfDud18Sksj4ZA; __cf_bm=cjqJzHzaxKtbgg14iM8uThOjR4vSkoN2ndg3Sf_xVCI-1791882592.0300267-1.0.1.1-2ZMU9owjLVXxBn218q1yzd1MbEhU12dDg_JBnrq0vd3cBCwpAPN8ppcHbjy8GvX1bFlZRJm02Vz0H0Rv1ISahvdP.nDbYj0W2G.h1azRYTz3X8b74biH1HrrZF4vYq_w; _cfuvid=usaufBU.F9PCQeAEAYNZFHVjfrl6dJ1huM.ZOuABFu4-1791882592.0300267-1.0.1.1-Q8.uBPoiQgPjc.UhvqOtwmY_tmkabilCT8yBboWWZ_8; timezoneOffset=-330',
}
Jobs=[]
offset=0
TotalJobs=0
while True :
    print('Offset----->',offset)
    json_data = {
        'appliedFacets': {},
        'limit': 20,
        'offset': offset,
        'searchText': '',
    }
    try:
        response = requests.post(
            'https://standard.wd1.myworkdayjobs.com/wday/cxs/standard/Search/jobs',
            # cookies=cookies,
            headers=headers,
            json=json_data,
        )
    except:
        time.sleep(0.5)
        response = requests.post(
                    'https://workday.wd5.myworkdayjobs.com/wday/cxs/workday/Workday/jobs',
                    # cookies=cookies,
                    headers=headers,
                    json=json_data,
                )

    print('Listing Page Status Code-------------->',response.status_code )

    #  Jobs.extend(response.json()['jobPostings'])
    desc_headers = {
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'priority': 'u=1, i',
    'referer': 'https://workday.wd5.myworkdayjobs.com/en-US/Workday/job/INDPune/Incident-Command-and-Observability-Lead_JR-0110219-1',
    'sec-ch-ua': '"Chromium";v="154", "Google Chrome";v="154", "Not A(Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/154.0.0.0 Safari/537.36',
    # 'x-calypso-csrf-token': '99c7b02d-1fb0-4d77-a6e8-9e8de4a76082',
    # 'cookie': 'PLAY_SESSION=81a028687878cc044c5cf5fdb268019fb0293fe7-workday_pSessionId=fd0shepeflient7i5fdgevofh2&instance=vps-prod-xw758zye.prod-vps.pr501.cust.pdx.wd; wd-browser-id=214bea74-6df2-4116-abdf-6fc512afd079; CALYPSO_CSRF_TOKEN=99c7b02d-1fb0-4d77-a6e8-9e8de4a76082; CALYPSO_SESSION=85f2c930-4f4f-42b2-a2b3-9cd3efb49bf7.d29ya2RheQ==.V0RDQzEuMIQAJQAAIJ/LyzvV2F/AbEOeXaeOdz/vWMFqO2KSFlHPac2e6scsAACMABYBMQAQ+llfZJUoMze4pgDm8ga9hAAAADg1ZjJjOTMwLTRmNGYtNDJiMi1hMmIzLTljZDNlZmI0OWJmNw==; wday_vps_cookie=669686794.53810.0000; __cflb=02DiuHJZe28xXz6hQKLf1exjNbMDM5uxfDud18Sksj4ZA; _cfuvid=usaufBU.F9PCQeAEAYNZFHVjfrl6dJ1huM.ZOuABFu4-1791882592.0300267-1.0.1.1-Q8.uBPoiQgPjc.UhvqOtwmY_tmkabilCT8yBboWWZ_8; timezoneOffset=-330; __cf_bm=F4ejoM8WCp_x8gfgVqjP_eRhx5O9gQHjxyjz17DT_es-1791884330.8533006-1.0.1.1-hsnTTWdEOWGrkU_sD4uC.5rzkpbwRp7y_ejZBzh7rdch2XcjuPA0IWS0qEyyBQV1Gcp23sQCFUBS2OVY3Im2Id_w6KX1tEGJcYNbzdZ9vkZ9qSbJYDn7k79dPBbUdJ.J',
}
    
    jobslist=response.json()['jobPostings']
    for job in jobslist :
       
            
        url='https://standard.wd1.myworkdayjobs.com/wday/cxs/standard/Search'+job['externalPath']
        try:
            desc_response= requests.get(url,headers= desc_headers)
        except:
            time.sleep(0.5)
            desc_response= requests.get(url,headers= desc_headers)
    

        print('Desc Res Status Code------>',desc_response.status_code)
        description_html=  desc_response.json()['jobPostingInfo']['jobDescription']
        enddate= desc_response.json()['jobPostingInfo'].get('endDate','')

       

        job['Description']=BeautifulSoup(description_html,'html.parser').text
        job['End Date']=enddate
        job['actualurl']='https://workday.wd5.myworkdayjobs.com/en-US/Workday'+ job['externalPath']
        Jobs.append(job)


    if offset==0:
        TotalJobs=response.json()['total']
    offset= offset+20
    
    if offset >= TotalJobs:
        break
 


    print(len(response.json()['jobPostings']))
with open('mywork_standard.json','w', encoding='utf-8') as f:
    json.dump(Jobs,f,indent=4,ensure_ascii=False) 