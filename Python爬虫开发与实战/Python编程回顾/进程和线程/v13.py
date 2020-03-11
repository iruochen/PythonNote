import time
from multiprocessing.managers import BaseManager
# 创建类似的QueueManger:
class QueueManager(BaseManager):
    pass

# 第一步：使用QueueManager注册用于获取Queue的方法名称
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# 第二步：连接到服务器
server_addr = '127.0.0.1'
print('Connect to server {}...'.format(server_addr))
# 端口和验证口令注意保持与服务器完全一致
m = QueueManager(address=(server_addr, 8001), authkey='ruochen')
# 从网络上连接
m.connect()

# 第三步：获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

# 第四步：从task队列获取任务，并把结果写入result队列
while(not task.empty()):
    image_url = task.get(True, timeout=5)
    print('run task download {}...'.format(image_url))
    time.sleep(1)
    result.put('{}--->success'.format(image_url))

# 处理结果
print('worker exit...')
