'''
使用参数headers和params
研究返回结果

'''
import requests

# 完整访问url是下面url加上参数构成
url = "http://www.baidu.com/s?"

kw = {
    "wd": "大熊猫"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code) # 请求返回码
