# encoding:utf-8

import requests
import base64

# client_id 为官网获取的AK， client_secret 为官网获取的SK
host = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='xLCMwgRClxarXX8zi8Yc4P05'&client_secret='aDqGdE0IRGq8NTXb4HdDM757ERulwBc4'"
response = requests.get(host)
if response:
    print(response)
'''
身份证识别
'''

# request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
# # 二进制方式打开图片文件
# f = open('E:/idcard/000.jpg', 'rb')
# img = base64.b64encode(f.read())

# params = {"id_card_side":"front","image":img}
# access_token = 'response.json()'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())