import requests

# url
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36',

}

data = {
    'cname': '',
    'pid': '',
    'keyword': '深圳',
    'pageIndex': '2',
    'pageSize': '5'
}

response = requests.post(url=url, data=data, headers=headers)

page_text = response.json()

for dic in page_text['Table1']:
    title = dic['storeName']
    addr = dic['addressDetail']
    print(title, addr)

