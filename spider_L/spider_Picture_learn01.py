import urllib3

import requests

pictureUrl = "https://img9.doubanio.com/view/photo/s_ratio_poster/public/p2168624214.webp"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}

# requests
response = requests.get(url=pictureUrl, headers=headers)

## content返回的是二进制形式的响应数据
imgData = response.content

with open("./img/pic.jpg", 'wb') as f:
    f.write((imgData))

# urllib3

http = urllib3.PoolManager()

# 可以直接对url发起请求并且进行持久化存储
img_url = "https://img-blog.csdnimg.cn/20201014180756913.png?x-oss-process=image/resize,m_fixed,h_64,w_64"

response_urllib = http.request("GET", img_url, headers=headers)
response_urllib.info()

with open("./img/pic2.jpg", 'wb') as f:
    f.write(response_urllib.data)
