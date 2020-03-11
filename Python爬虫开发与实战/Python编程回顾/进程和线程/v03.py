# pool类进程池案例
from multiprocessing import Pool
import os, time, random


def run_task(name):
    print('Task {} (pid={}) is running...'.format(name, os.getpid()))
    # random.random() 生成(0, 1)随机浮点型数
    time.sleep(random.random() * 3)
    print('Task {} end'.format(name))


if __name__ == '__main__':
    print('Current process {}'.format(os.getpid()))
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done...')