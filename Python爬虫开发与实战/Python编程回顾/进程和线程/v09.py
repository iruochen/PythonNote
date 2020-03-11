from gevent import monkey; monkey.patch_all()
import gevent
import urllib.request

def run_task(url):
    print('Visit --> %s' % url)
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        print('%d bytes received from %s.' % (len(data), url))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    urls = {'https://github.com/', 'https://www.python.org/', 'https://www.cnblogs.com/'}
    # spawn: 形成协程
    greenlets = [gevent.spawn(run_task, url) for url in urls]
    # joinall: 添加协程任务，并且启动运行
    gevent.joinall(greenlets)
