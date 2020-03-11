import requests
import os

url = 'http://image.biaobaiju.com/uploads/20180919/14/1537338335-xcyRldrnPY.jpg'
root = 'pics'
path = root + '/' + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存完成')
    else:
        print('文件已经存在')

except Exception as e:
    print('爬取失败')
    print(e)
