import random
import time, threading

# 新线程执行代码
def thread_run(urls):
    print('Current {} is running...'.format(threading.current_thread().name))
    for url in urls:
        print('{} ------->> {}'.format(threading.current_thread().name, url))
        time.sleep(random.random())
    print('{} ended...'.format(threading.current_thread().name))

print('{} is running...'.format(threading.current_thread().name))
t1  = threading.Thread(target=thread_run, name='Thread_1', args=(['url_1', 'url_2', 'url_3'], ))
t2  = threading.Thread(target=thread_run, name='Thread_2', args=(['url_4', 'url_5', 'url_6'], ))
t1.start()
t2.start()
t1.join()
t2.join()
print('{} ended...'.format(threading.current_thread().name))
