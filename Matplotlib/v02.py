'''
图形中文显示
'''

from matplotlib import pyplot as plt
import matplotlib
import numpy as np

# 打印font_manager 的 ttflist 中所有注册的名字
'''
a = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
for i in a:
    print(i)
'''

# 创建x轴上的值
x = np.arange(1, 11)
# y轴上的值
y = 2 * x + 5
plt.rcParams['font.family'] = ['STFangsong']
plt.title('直线')
plt.xlabel('x 轴')
plt.ylabel('y 轴')
# 绘制
plt.plot(x, y, 'or')
# 显示
plt.show()
