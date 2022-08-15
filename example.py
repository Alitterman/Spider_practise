import requests

url ="http://preview.qiantucdn.com/58pic/35/92/62/03558PICP58PIC58PIC02NZ3V62cx_PIC2018.jpg!qt324new_nowater"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
}

page = requests.request("GET", url=url, headers=headers)
print(page.text)