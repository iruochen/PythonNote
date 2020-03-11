url = 'https://www.baidu/#/111'
print(url)
if '#' in url:
    url = url.replace('#/', '')
print(url)