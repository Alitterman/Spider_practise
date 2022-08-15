import requests

import xlwt


def main():
    baseurl = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"

    new_url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?hKHnQfLv=5vXdPIjOEt3w74ycTnVGgDjEbZQy7dboHJRU53kyyJ2XS4Asd3Vx1y96_cVNRitkC8AfgQYsExPyP4uMTmVXq9e32fz1z1gFiH6tCawBkZwhKhvlC_X4XIU6itNKmxLWqtT0OhoqZ4HdLTqQrQI0R3eYdFn75taf6rz3Tbw5rGp2dXiooh_2m56lQfXGj5NpfyPCBkQZn.ermSVgLj0airvR0g0y95LOnMRbbj33m1eG0TLPJWCz9.ppyCM0mOl7D3xtRLJ1MA2Tg_ZEEuAHYGuEPxU9fjYjtvsT4pcxG88YpzV0ZSY0grO_4FAsNi0wC&8X7Yi61c=4TeDHZ7.uWxHLYKHjqPbLAphj4xsXqg7GpE7QsqN4ex2jqF2upsCLMD8wYFvasrvQzvnYzAUGslGpuabYkCYbTx4Ik74mCZU62VvKrjcOcKOtDTTgtnrmRk0toXGZXgNH"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    }
    data = {
        "id":"8947d95996154fd9b87c1ad7c0d0113a"
    }

    response = requests.post(url=new_url, headers=headers)
    print(response.status_code)
    print(response.json())
#     datalist = []
#     for page in range(1, 6):
#         data = {
#             'on': 'true',
#             'page': str(page),
#             'pageSize': '15',
#             'productName': '',
#             'conditionType': '1',
#             'applyname': '',
#             'applysn': ''
#         }
#         response = requests.post(url=baseurl, data=data, headers=headers)
#         print(response.status_code)
#
#         page_text = response.json()
#         for dic in page_text['list']:
#             item = []
#             id = dic['ID']
#             data = {
#                 'id': str(id)
#             }
#             response = requests.post(url=url, data=data, headers=headers)
#             page_text = response.json()
#             # print(page_text)
#
#             epsName = page_text['epsName']
#             item.append(epsName)
#
#             productSn = page_text['productSn']
#             item.append(productSn)
#
#             certStr = page_text['certStr']
#             item.append(certStr)
#
#             epsAddress = page_text['epsAddress']
#             item.append(epsAddress)
#
#             epsProductAddress = page_text['epsProductAddress']
#             item.append(epsProductAddress)
#
#             businessLicenseNumber = page_text['businessLicenseNumber']
#             item.append(businessLicenseNumber)
#
#             legalPerson = page_text['legalPerson']
#             item.append(legalPerson)
#
#             businessPerson = page_text['businessPerson']
#             item.append(businessPerson)
#
#             qualityPerson = page_text['qualityPerson']
#             item.append(qualityPerson)
#
#             qfManagerName = page_text['qfManagerName']
#             item.append(qfManagerName)
#
#             xkName = page_text['xkName']
#             item.append(xkName)
#
#             rcManagerDepartName = page_text['rcManagerDepartName']
#             item.append(rcManagerDepartName)
#
#             rcManagerUser = page_text['rcManagerUser']
#             item.append(rcManagerUser)
#
#             xkDate = page_text['xkDate']
#             item.append(xkDate)
#
#             xkDateStr = page_text['xkDateStr']
#             item.append(xkDateStr)
#
#             datalist.append(item)
#     print(datalist)
#     savepath = "NMPA化妆品生产许可信息数据.xls"
#     saveData(datalist, savepath)
#
#
# def saveData(datalist, savepath):
#     print("开始保存...")
#     book = xlwt.Workbook(encoding="utf-8", style_compression=0)
#     sheet = book.add_sheet('NMPA化妆品生产许可信息数据', cell_overwrite_ok=True)
#     col = ("企业名称", "许可证编号", "许可项目", "企业住所", "生产地址", "社会信用代码", "法定代表人", "企业负责人",
#            "质量负责人", "发证机关", "签发人", "日常监督管理机构", "日常见度管理人员", "有效期至")
#     for i in range(0, 14):
#         sheet.write(0, i, col[i])
#     for i in range(0, 75):
#         print("第%d条" % (i + 1))
#         data = datalist[i]
#         for j in range(0, 14):
#             sheet.write(i + 1, j, data[j])
#     book.save(savepath)
#     print("保存完成")




if __name__ == "__main__":
    main()
