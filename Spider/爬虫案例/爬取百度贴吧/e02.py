from urllib import request, parse
import time
import os

if __name__ == '__main__':

    name = input("贴吧名字：")
    start = int(input("起始页码："))
    end = int(input("终止页码："))

    qs = {
        'kw': name,
        'ie': 'utf-8',
        'pn': 0
    }
    baseurl = "https://tieba.baidu.com/f?"

    for page in range(start, end+1):
        pn = (page-1) * 50
        qs['pn'] = str(pn)
        query_string = parse.urlencode(qs)
        new_url = baseurl + query_string
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        }
        req = request.Request(new_url)
        req.add_header( 'User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36')
        # 创建文件夹
        if not os.path.exists(name):
            os.mkdir(name)
        rsp = request.urlopen(req)
        filename = '%s-第%s页.html'%(name, page)
        filepath = os.path.join(name, filename)
        print("正在下载------------{0}第{1}页".format(name, page))
        # 下载内容写入文件
        with open(filepath, 'wb') as f:
            f.write(rsp.read())
        time.sleep(3)

    print("{}-------下载完成".format(name))





