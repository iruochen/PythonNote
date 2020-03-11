'''
绘制正弦波
'''
import numpy as np
import matplotlib.pyplot as plt

# subplot() 函数允许在同一图中绘制不同的东西
# 计算正弦曲线上的 x 和 y 坐标
x = np.arange(0, 2 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.rcParams['font.family'] = ['STFangsong']
# 建立 subplot 网络，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2, 1, 1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('正弦曲线')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('余弦曲线')
# 展示图像
plt.show()
