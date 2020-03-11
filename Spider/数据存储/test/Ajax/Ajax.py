'''
Ajax异步加载

https://www.pexels.com/search/beautiful%20girl/?page=1
'''

import requests, re
from bs4 import BeautifulSoup
import random
ip_list = [
    {'http': '113.195.155.53:9999'},
    {'https': '49.76.193.47:9999'},
    {'http': '60.176.10.81:8118'},
    {'http': '117.88.177.182:3000'},
    {'http': '182.46.115.54:9999'}
]
# ip = random.choice(ip_list)

headers = {
    'cookie': '__cfduid=d1cba04b59592c605e2c6631d79fc9a891581950393; locale=en-US; _ga=GA1.2.997534047.1581950396; _gid=GA1.2.1935114976.1581950396; _hjid=afd03f92-e189-4d0f-b10f-0ccf59e0cda1; _fbp=fb.1.1582005682428.1308395283',
    'Accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

title = input('Please input you want to search: ')
urls = ['https://www.pexels.com/search/' + str(title) + '/?page={}'.format(str(i)) for i in range(1, 2)]
print(urls)
photos = []

for url in urls:
    response = requests.get(url, headers=headers, proxies=random.choice(ip_list))
    print(response.text)
    soup = BeautifulSoup(response.text, 'lxml')
    imgs = soup.select('article > a > img')
    # print(imgs)
    for img in imgs:
        photo = img.get('scr')
        # print(photo)
        if photo.endswith('350'):
            photos.append(photo)


path = 'img'
for item in photos:
    data = requests.get(item, headers=headers)
    photo_name = re.findall('\d+\/(.*?)\?', item)
    if photo_name:
        fp = open(path+'/'+photo_name[0], 'wb')
        fp.write(data.content)
        fp.close()


