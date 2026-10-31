import requests

cookies = {
    'wd-browser-id': '214bea74-6df2-4116-abdf-6fc512afd079',
    'CALYPSO_CSRF_TOKEN': '99c7b02d-1fb0-4d77-a6e8-9e8de4a76082',
    'wday_vps_cookie': '669686794.53810.0000',
    '__cflb': '02DiuHJZe28xXz6hQKLf1exjNbMDM5uxfDud18Sksj4ZA',
    'timezoneOffset': '-330',
    'PLAY_SESSION': 'fe51f6a6dc2b8e292c00694ec971f78a3cb77871-workday_pSessionId=eb6j35aj8n88e7haptf1kfqjuc&instance=vps-prod-xw758zye.prod-vps.pr501.cust.pdx.wd',
    'CALYPSO_SESSION': '502609e9-0b39-4412-af2b-8ea3485a55a1.d29ya2RheQ==.V0RDQzEuMIQAJQAAIEHoybdx6P2Wp7lBxpkIX6gJqFe7VN6NctDHAqgFqTy5AACMABYBMQAQSFhmz35dEAFvTHY8qaahwAAAADUwMjYwOWU5LTBiMzktNDQxMi1hZjJiLThlYTM0ODVhNTVhMQ==',
    '__cf_bm': '.Z4q8PP6YvSrWdfSChHAoTunMRO1F59dY2UvFtuuUD8-1791961420.7986865-1.0.1.1-Do0xFi2.IhJic9X6WSgr_pX.SU4zmKzKrJdQKaSaGoJ4eW3D1O3vhPWgPKd_wG10ZyI_DZ.OCpyl4fLKJ4QvKwGcN6GdbdCPmZ.OYW9PLm2oXKZhGSwnvIyBkERtJ2yA',
    '_cfuvid': 'icoy_REXOpc6zmJqTvxlXOzHvqfh8ljDzEU_zr7M9bU-1791961420.7986865-1.0.1.1-0ni3XFJIfT1ZX.mhKgGpjqRSK8elPcdSJpXL77d9X_I',
}

headers = {
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
    # 'cookie': 'wd-browser-id=214bea74-6df2-4116-abdf-6fc512afd079; CALYPSO_CSRF_TOKEN=99c7b02d-1fb0-4d77-a6e8-9e8de4a76082; wday_vps_cookie=669686794.53810.0000; __cflb=02DiuHJZe28xXz6hQKLf1exjNbMDM5uxfDud18Sksj4ZA; timezoneOffset=-330; PLAY_SESSION=fe51f6a6dc2b8e292c00694ec971f78a3cb77871-workday_pSessionId=eb6j35aj8n88e7haptf1kfqjuc&instance=vps-prod-xw758zye.prod-vps.pr501.cust.pdx.wd; CALYPSO_SESSION=502609e9-0b39-4412-af2b-8ea3485a55a1.d29ya2RheQ==.V0RDQzEuMIQAJQAAIEHoybdx6P2Wp7lBxpkIX6gJqFe7VN6NctDHAqgFqTy5AACMABYBMQAQSFhmz35dEAFvTHY8qaahwAAAADUwMjYwOWU5LTBiMzktNDQxMi1hZjJiLThlYTM0ODVhNTVhMQ==; __cf_bm=.Z4q8PP6YvSrWdfSChHAoTunMRO1F59dY2UvFtuuUD8-1791961420.7986865-1.0.1.1-Do0xFi2.IhJic9X6WSgr_pX.SU4zmKzKrJdQKaSaGoJ4eW3D1O3vhPWgPKd_wG10ZyI_DZ.OCpyl4fLKJ4QvKwGcN6GdbdCPmZ.OYW9PLm2oXKZhGSwnvIyBkERtJ2yA; _cfuvid=icoy_REXOpc6zmJqTvxlXOzHvqfh8ljDzEU_zr7M9bU-1791961420.7986865-1.0.1.1-0ni3XFJIfT1ZX.mhKgGpjqRSK8elPcdSJpXL77d9X_I',
}

response = requests.get(
    'https://workday.wd5.myworkdayjobs.com/wday/cxs/workday/Workday/job/INDPune/Incident-Command-and-Observability-Lead_JR-0110219-1',
    # cookies=cookies,
    headers=headers,
)
print(response.status_code)
print(response.json())