import os
import re


import requests

'''
通过get方法请求网页

:param url 请求url

:return page 返回请求体
:rtype requsts.response
'''
def request_Get(url,headers={},data={}, **kwargs):
    if not headers:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }
    data = {
        'Cookie': 'BAIDUID=FDD8088AD023B282BD28DB7D2CA5B755:FG=1; PSTM=1660210661; BIDUPSID=0C602C0C8ADA942911644A9B60440CA1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=PTuOJexroG0mXfODUsUWUGk832KKvV3TDYLEOwXPsp3LGJLVc8u-EG0PtoaGdu_-ox8EogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=JnCH_DDhJKt3fP36q4ofK4_WKUnh-I62aJ0tW-bvWJ5TMCoYMxnVD-Iv3tnBJpQx2b-ehpTuLqr_ShPC-tPW0t0Y5PRIWM3R5Kkj5hOo3l02V-T9e-t2ynLIXJJXQ4RMW20e0h7mWIbmsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCajTcQjN_qq-jeHDrKBRbaHJOoDDv15ROcy4LbKxnxJPrv5eOR-4OwKf5njIPRDxRv5l5y3-OkWUQ9babTQ-tbBp3k8MQneb_VQfbQ0hOy5xbbbG8LW-Py3R7JOpkRbUnxy50rQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6IDJbKj_KKKfbo5KRopMtOhq4tehHRTLnQ9WDTOQJ7Ttn6iel7e3Jbl3pL1MNAeJfnibHFe-pbwBp5cfUnMKn05XM-pXbj2qnLL3mkjbPbOKl3fffAzhnAWQt4syP4eKMRnWnnTKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5AWjTvP; H_PS_PSSID=36555_36460_36975_36954_36948_36918_36569_36805_36776_37078_37128_37134_37055_26350_37088; BDSFRCVID_BFESS=PTuOJexroG0mXfODUsUWUGk832KKvV3TDYLEOwXPsp3LGJLVc8u-EG0PtoaGdu_-ox8EogKK3gOTH4PF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BA_HECTOR=25202kak0480a0200k2k32p91hfjrqb16; delPer=0; PSINO=7; BAIDUID_BFESS=FDD8088AD023B282BD28DB7D2CA5B755:FG=1; H_BDCLCKID_SF_BFESS=JnCH_DDhJKt3fP36q4ofK4_WKUnh-I62aJ0tW-bvWJ5TMCoYMxnVD-Iv3tnBJpQx2b-ehpTuLqr_ShPC-tPW0t0Y5PRIWM3R5Kkj5hOo3l02V-T9e-t2ynLIXJJXQ4RMW20e0h7mWIbmsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJIjjCajTcQjN_qq-jeHDrKBRbaHJOoDDv15ROcy4LbKxnxJPrv5eOR-4OwKf5njIPRDxRv5l5y3-OkWUQ9babTQ-tbBp3k8MQneb_VQfbQ0hOy5xbbbG8LW-Py3R7JOpkRbUnxy50rQRPH-Rv92DQMVU52QqcqEIQHQT3m5-5bbN3ut6IDJbKj_KKKfbo5KRopMtOhq4tehHRTLnQ9WDTOQJ7Ttn6iel7e3Jbl3pL1MNAeJfnibHFe-pbwBp5cfUnMKn05XM-pXbj2qnLL3mkjbPbOKl3fffAzhnAWQt4syP4eKMRnWnnTKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCcjqR8Zj5AWjTvP; ZFY=PYDpDkGuI5IZD89cEqiu6Qcr2KIURp1CncUSTzLAxP0:C; BDRCVFR[Q5XHKaSBNfR]=mk3SLVN4HKm; BDRCVFR[X_XKQks0S63]=mk3SLVN4HKm; RT="z=1&dm=baidu.com&si=7g0b2sfuqyj&ss=l6ufgntk&sl=0&tt=0&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ul=11v&hd=12b"; ab_sr=1.0.1_ODNhZjI5NWUyYzJkZGI2NTRkOGNhYWEwOTg2N2RjODMwZmNiOTMwNDlhZThkMDE2NWIyNzFmMzU3YzEzNGIzODY3MTZlYmVmMjU0NmM1OWNiZWE4YTI3MWExMWRhNzlhYzFhODZhOTA2YjBmNjRmYmI4MWEzYjJiNzIyMzA3ODAyYTA4OWI3MWVlYjBjMTQ2YTdiZDllNTVlMjFlM2RlYg==; userFrom=null'
    }

    page = requests.request("GET", url=url, headers=headers)

    return page


def re_src(ex,page):
    '''
       正则匹配

       '''
    ex_data_original = '<img class="lazy" data-original="//(.*?)" .*?/>'
    ex_src = '<img class="lazy" .*? src="//(.*?)".*?/>'

    img_List_1 = re.findall(ex_data_original, page, re.S)
    img_List_2 = re.findall(ex_src, page, re.S)
    img_List = img_List_1 + img_List_2

    print(img_List)


'''
文件存放目录检测与创建 
'''
def creat_ImgFile():
    dirName = 'ImgLibPics'
    if not os.path.exists(dirName):
        os.mkdir(dirName)
    dirName = 'ImgLibs'
    if not os.path.exists(dirName):
        os.mkdir(dirName)


if __name__ == "__main__":





    '''
    放入网页端浏览图片
    '''
    i = 0
    # for src in img_List:
    #     i = i+1
    #     src = "https://" + src
    #     with open("./ImgLibs/"+str(i)+"_img.html", "w") as f:
    #         f.write('"<img src="' + src + '"/>')


    '''
    直接将图片以jpg形式保存到本地
    
    '''
    # for src in img_List:
    #     src = "https://" + src
    #     print("图片",src,"已下载")
    #     i = i+1
    #     page = request_Get(src)
    #     with open("./ImgLibPics./"+ str(i) +"_img.jpg", "wb") as f:
    #         f.write(page.content)
