'''
利用selenium模拟登陆豆瓣
需要输入验证码
思路：
1. 保存页面成快照
2. 等待用户手动输入验证码
3. 继续自动执行提交等动作

# 貌似已经没有验证码了
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://accounts.douban.com/passport/login"
driver = webdriver.Chrome()
driver.get(url)

time.sleep(4)

# 生成快照，用来查看验证码
driver.save_screenshot('douban_index.png')

# 利用账户信息登陆
driver.find_element_by_id('username').send_keys('18203503747')
driver.find_element_by_id('password').send_keys('ruochen666')

# driver.find_element_by_class_name('btn btn-account').click()

# driver.find_element_by_xpath('//a[@class="btn btn-account"]').click()
time.sleep(5)

driver.save_screenshot('logined.png')

with open('douban_home.html', 'w', encoding='utf-8') as f:
    f.write(driver.page_source)

driver.quit()
