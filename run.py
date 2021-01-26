from commen import method   # 导入公共方法
from test_data import test_data
from selenium import webdriver
driver = webdriver.Chrome()   # 初始化浏览器后续操作都是基于这个浏览器  --会话session
driver.implicitly_wait(10)   # 隐性等待

url=test_data.data['url']
username=test_data.data['username']
password=test_data.data.get('password')
key=test_data.data.get('key')
print(driver,url,username,password,key)
num = method.sear_fun(driver,url,username,password,key)
if key in num:
    print("搜索用例通过")

else:
    print("搜索失败")