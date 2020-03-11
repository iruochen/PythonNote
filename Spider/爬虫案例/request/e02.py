import requests
url = 'https://www.12306.cn/otn/'
# 免ssl认证
res = requests.get(url, verify=True)
print(res.text)