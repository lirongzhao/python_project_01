import time
def open_url(driver,url):
    driver.get(url)  # 打开浏览器对应的网址
    driver.maximize_window()

def login_fun(driver,username,password):
    # 输入用户名和密码进行操作
    driver.find_element_by_id('username').send_keys(username)
    # time.sleep(1)
    driver.find_element_by_id('password').send_keys(password)
    # time.sleep(1)
    driver.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    driver.find_element_by_id("btnSubmit").click()
# 搜索函数
def sear_fun(driver,url,username,password,key):
    open_url(driver,url)
    login_fun(driver,username,password)
    # 零售出库
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    time.sleep(2)
    # 切换到子页面   id是变化的，就不能直接使用
    # driver.switch_to.frame("tabpanel-b052a3cbea-frame")
    id_li = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")  # 找到元素并获取id属性
    # print(id_li)
    id_frame = id_li+'-frame'
    driver.switch_to.frame(id_frame)
    # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))  # 通过web element切换子页面
    # 接下来
    driver.find_element_by_id("searchNumber").send_keys(key)  # 找到搜索输入数据
    driver.find_element_by_id("searchBtn") .click() # 点击查询按钮
    time.sleep(1)  # 隐式等待+强制等待
    # 报错 表达式出错  页面没有加载出来(加个等待)
    # 获取
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
