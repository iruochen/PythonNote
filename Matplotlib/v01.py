'''
直线绘制案例
'''
from matplotlib import pyplot as plt
import numpy as np

# 创建x轴上的值
x = np.arange(1, 11)
# y轴上的值
y = 2 * x + 5
plt.title('Matplotlib demo')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
# 绘制
plt.plot(x, y)
# 显示
plt.show()