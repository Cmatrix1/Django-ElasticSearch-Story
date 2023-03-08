import requests

cookies = {
    'csrftoken': 'HHf4pLEAW68CRL8UbGGY8syY7PvvX45dqHdvzlstHMlnwvDWoySk25TN4Xa9AfzF',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    # 'Cookie': 'csrftoken=HHf4pLEAW68CRL8UbGGY8syY7PvvX45dqHdvzlstHMlnwvDWoySk25TN4Xa9AfzF',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

for i in range(22000):
    response = requests.get('http://127.0.0.1:8000/story/'+str(i), cookies=cookies, headers=headers)
    print(i)