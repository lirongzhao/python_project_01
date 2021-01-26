"""
自动化类型：
接口自动化： --接口最多，稳定，性价比最高  == 回归测试 80%+
UI自动化： 改动频繁，性价比低，做 维护成本高  ==冒烟测试 30%+
APP自动化：

（web）UI自动化：
人  ----  浏览器之间的互动
(python)代码 --翻译（中间人）-- 浏览器之间的互动  ：驱动可以把代码的指令翻译给浏览器，浏览器可以做响应的操作
      浏览器驱动
      chromedriver（谷歌驱动 71版本） 低版本驱动可以适用高版本的浏览器
      geckoddriver（火狐驱动）
      ieserverdriver(ie驱动)

selenium工具包：UI自动化工具 --第三方库  如何使用？？安装 并 盗用
包括三个部分：
1.ide--录制脚本--少，不好用，不太准确 -- 需要手工修改
2.webdriver:库--提供了对网页的各种操作的方法（点击，滑动，等等），也提供了各种语言版本（python，Java等） ===必须结合语言来用
3.grid:分布式测试--同时对多个浏览器执行并发的---官方文档

1.selenium 安装好
2.驱动下载--python对应的安装目录 --浏览器安装对的
3.导入selenium webdriver

通讯原理：
1、chromedrive启动服务  IP地址 端口  监听
2、python webdriver 和 chromedrive 建立连接，发送http请求
3、chromedriver 收到 指令之后，驱动浏览器把指令执行
4.chromedriver 要把执行结果返回给chromedriver
后续指令重复此操作
"""
from selenium import webdriver
import time
driver = webdriver.Chrome()   # 初始化浏览器后续操作都是基于这个浏览器  --会话session
driver.get("https://baidu.com")  # 打开浏览器对应的网址
# 浏览器最大化
driver.maximize_window()
driver.get("https://taobao.com")
time.sleep(2)
driver.back()  # 返回上一个页面
time.sleep(2)
driver.forward()  # 前进一个页面
time.sleep(2)
driver.refresh()  # 刷新当前页面

# 关闭浏览器：
# close():关闭浏览器窗口，不会退出浏览器
# quit()：退出当前会话，并关闭浏览器，清除缓存
driver.close()