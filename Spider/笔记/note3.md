# 正则表达式
- 一套规则，可以在字符串文本中进行搜查替换等
- 案例v38


# 动态HTML

## 爬虫跟反爬虫

## 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从JavaScript代码入手采集
    - Python第三方库运行JavaScript，直接采集你在浏览器看到的页面
   
## Selenium + PhantomJS
- Selenium：web自动化测试工具     
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install selenium==2.48.0
    - [官网](https://selenium-python.readthedocs.io/)
    - [中文文档](https://selenium-python-zh.readthedocs.io/en/latest/)
- PhantomJS(幽灵)
    - 基于webkit 的无界面浏览器
    - [官网](http://phantomjs.org/download.html)
- Selenium 库有一个WebDriver的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例v39
- chrome + chromedriver
    - 下载安装chrome：下载+安装
    - 下载安装chromedriver：
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by_xpath        
        - find_elements_by_link_text        
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 可以通过导入ActionsChains类来做到
    - 案例v40
    
# 验证码问题
- 验证码：防止机器人或者爬虫
- 分类：
    - 简单图片
    - 极验：[官网](www.geetest.com)
    - 12306
    - 电话
    - google验证

- 验证码破解：
    - 通用方法：
        - 下载网页和验证码
        - 手动输入验证码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用[第三方图像验证码破解网站](www.chaojiying.com)
    - 极验：[官网](www.geetest.com)
        - 破解比较麻烦
        - 可以模拟鼠标等移动
        - 一直在进化
    - 12306
    - 电话：语音识别
    - google验证

# Tesseract
- 机器视觉领域的基础软件
- OCR：OpticalChracterRecognition，光学文字识别
- Tesseract：一个ocr库，有google资助
- 安装：
    - Windows：https://jingyan.baidu.com/article/219f4bf788addfde442d38fe.html
    - Mac：brew install tesseract
    - Linux：
        - apt-get install tesseract-ocr
        - aptitude install tesseract-ocr
    - 安装完成后需要设置环境变量
- 安装完成后还需要pytesseract
    - pip install pytesseract
    
- 读取案例
    - 案例v41
