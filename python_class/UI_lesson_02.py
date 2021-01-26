"""
https://blog.csdn.net/ran2017/article/details/109609878?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-2&spm=1001.2101.3001.4242
ERP：企业资源管理

web页面基本组成--html页面： HTML+CSS+JS
html：定义页面呈现内容 标签语言   <>值</>
CSS:控制页面布局   字体颜色，字体大小
js:可以让页面在不同情形下做不同的事情
html页面： 标签--属性
页面元素定位：能够唯一标识这个元素的内容(8种id,name,xpath    css，class，tag，link，partial_link)
按照开发遵循的原则--元素属性里 id name 基本是唯一的
通过id 进行元素定位
id: username
id: password
通过id,name找到这个元素.  但是大部分的元素没有这两个属性，使用xpath    css，class，tag，link，partial_link等等
注意：如果id是变化的，就不能直接使用
Xpath元素定位方法：
1.绝对路径：在浏览器F12查看元素代码，复制xpath路径    /html/body/div[1]/aside/div/section/div[1]/div[2]/p
（--从根开始，一级一级往下找--继承，顺序，所以页面一旦发生变化，修改代码==不好用，用的少！  基本不用绝对路径）
相对路径： // --以//开头。不考虑层级关系，靠自己（如果不唯一了）
偶尔靠一下上级标签，上上级标签   ---相对路径用的更多
2.层级定位：
//input[@name="username"]    属性尽可能有标识性
//div[@class="login-logo"]//b
3.文本属性定位  //b[text()="柠檬ERP"]      ---当值不变的，是唯一标识的
4.当标签值太长不好标识时，可以用contains包含，写值的关键字就可以
//b[contains(text(),"柠檬")]
//div[contains(@class,"logo")]//b
5.轴定位方法：
通过兄弟来找自己
//input[@id="rememberUserCode"]/following-sibling::ins            ****的后面
//*******/preceding-sibling::                    *****的前面
找到元素之后的操作：
点击：click
输入内容：send_keys()
获取文本内容：text
获取属性：attribute --id，class属性

三大等待
python等待：  一般click操作之后，页面刷新时间  --加个等待时间
1.强制等待  --sleep() 设置等待时长--没到期，就算元素出现了，也还要继续等待
2.智能等待 ：
    1）隐性等待： 会有一个默认等待时间，只要等到元素出现，直接继续往下执行  ===一个会话只执行一次就行
    设置默认等待时间，提前出现提前执行  --有些地方不生效，+ 自己再加上强制等待
    2）显示等待（复杂）
"""

from selenium import webdriver
import time
driver = webdriver.Chrome()   # 初始化浏览器后续操作都是基于这个浏览器  --会话session
driver.implicitly_wait(10)   # 隐性等待
driver.get("http://erp.lemfix.com")  # 打开浏览器对应的网址
# 浏览器最大化
driver.maximize_window()
# 获取页面标题
page_title = driver.title
if page_title == '柠檬ERP':
    print("这个页面标题是{}".format(page_title))
else:
    print(("这个页面标题不是{}，用例不通过".format(page_title)))

# 输入用户名和密码进行操作
driver.find_element_by_id('username').send_keys("test123")
# time.sleep(1)
driver.find_element_by_id('password').send_keys("123456")
# time.sleep(1)
driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
driver.find_element_by_id("btnSubmit").click()
# time.sleep(2)
# 确认登录
page_name = driver.find_element_by_xpath("//p").text   # 获取这个元素的文本内容
if page_name == '测试用户':
    print("这个登录用户是{}".format(page_name))
else:
    print("这个用例不通过{}".format(page_name))

# 零售出库
driver.find_element_by_xpath("//span[text()='零售出库']").click()
time.sleep(2)
# 切换到子页面   id是变化的，就不能直接使用
# driver.switch_to.frame("tabpanel-b052a3cbea-frame")
id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")  # 找到元素并获取id属性
# print(id_li)
id_frame = id_li+'-frame'
# driver.switch_to.frame(id_frame)
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))  # 通过web element切换子页面
# 接下来
driver.find_element_by_id("searchNumber").send_keys("841")  # 找到搜索输入数据
driver.find_element_by_id("searchBtn") .click() # 点击查询按钮
time.sleep(1)  # 隐式等待+强制等待
# 报错 表达式出错  页面没有加载出来(加个等待)
"""
html里--嵌套了html--子页面，直接定位元素是不行的
如何识别？ 1.在页面里找子html 2.识别路径--只要包含了iframe
如何切换子页面:
1.frame名字 --唯一标识 ==id，name，   用的最多
2.元素定位方式  通过web element切换子页面 次之
3.下标

提高代码复用率：
封装
自动化框架
"""
# 获取
num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
print(num)
if '841' in num:
    print('搜索用例通过')
else:
    print('搜索失败')