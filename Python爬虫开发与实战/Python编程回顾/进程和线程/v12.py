'''
Windows版本
'''
# coding:utf-8
import random, time
from queue import Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 任务个数
task_number = 10
# 定义收发队列
task_queue = Queue(task_number)
result_queue = Queue(task_number)

def get_task():
    return task_queue
def get_result():
    return result_queue

class Queuemanager(BaseManager):
    pass

def win_run():
    # Windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    Queuemanager.register('get_task_queue', callable=get_task)
    Queuemanager.register('get_result_queue', callable=get_result)

    # 绑定端口并设置口令，Windows下需要填写IP地址，Linux下不填默认为本地
    manager = Queuemanager(address=('127.0.0.1',8001), authkey='ruochen')
    # 启动
    manager.start()
    try:
        # 通过网络获取任务队列和结果队列
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 添加任务
        for url in ['ImageUrl_' + str(i) for i in range(10)]:
            print('put task {}...'.format(url))
            task.put(url)
        # 获取返回结果
        print('try get result...')
        for i in range(10):
            print('result is {}'.format(result.get(timeout=10)))
    except:
        print('Manager error')
    finally:
        # 一定要关闭，否则会报管道未关闭的错误
        manager.shutdown()

if __name__ == '__main__':
    # Windows下多进程可能会有问题，添加这句可以缓解
    freeze_support()
    win_run()
