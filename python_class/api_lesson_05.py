import requests
import pprint
import jsonpath
""" 
# 注册接口
url_api_reg="http://8.129.91.152:8766/futureloan/member/register"
api_data_reg={
    "mobile_phone": "15703286212",
    "pwd": "12345678",
    "type": "1",
    "reg_name": "mengmeng"
}
head_reg = {"X-Lemonban-Media-Type": "lemonban.v2"}
response_reg = requests.post(url=url_api_reg, json=api_data_reg, headers=head_reg)
print(response_reg.json())
"""

"""
# 登录接口
url_api_login="http://8.129.91.152:8766/futureloan/member/login"
api_data_login={
    "mobile_phone":"15703286212",
    "pwd":"12345678",
}
head_login = {"X-Lemonban-Media-Type":"lemonban.v2"}
response_login = requests.post(url=url_api_login,json=api_data_login,headers=head_login)
res = response_login.json()
pprint.pprint(res)

# 充值接口
url_api_recharge="http://8.129.91.152:8766/futureloan/member/recharge"
# 字典取值 --接口关联
# member_id = res['data']['id']
# token = res['data']['token_info']['token']
# api_data_recharge={
#     "member_id": member_id,
#     "amount": 6300
# }
# jsonpath取值:安装第三方库并导入    $代表json的最外层  返回结果放到了一个列表里
# ..两个点代表匹配任意次
# member_id=jsonpath.jsonpath(res,"$.data.id")[0]
# token =jsonpath.jsonpath(res,"$.data.token_info.token")[0]
member_id=jsonpath.jsonpath(res,"$..id")[0]
token =jsonpath.jsonpath(res,"$..token")[0]
api_data_recharge={
    "member_id": member_id,
    "amount": 2700
}
head_recharge = {"X-Lemonban-Media-Type":"lemonban.v2","Authorization": 'Bearer '+token}
response_rec = requests.post(url=url_api_recharge,json=api_data_recharge,headers=head_recharge)
pprint.pprint(response_rec.json())

# jsonpath
"""

# python+requesrs库 测试
# 访问百度请求--扩展
# 1.乱码  --手动指定解码
# 2.不是一个正确的页面 --爬虫 --好多网站有反爬机制，检查请求不是正规浏览器发过来，不会正确响应
# User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36
# https://www.baidu.com/s?wd=柠檬班
url_baidu = "https://www.baidu.com/"
head = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
param = {"wd": "柠檬班"}
res = requests.get(url=url_baidu, headers=head, params=param)  # 响应类型是text/html
# print(res.text) # 自动解码页面，不能解码成功的话再用另外一种方法（手动指定解码）
print(res.content.decode("utf-8"))  # 手动指定解码
