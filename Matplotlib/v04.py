'''
pyplot 子模块的 bar() 函数来生成条形图
'''
import matplotlib.pyplot as plt

x = [5, 8, 10]
y = [12, 16, 6]
x2 = [6, 9, 11]
y2 = [6, 15, 7]
plt.bar(x, y, color='r', align='center')
plt.bar(x2, y2, color='g', align='center')
plt.title('Bar graph')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()
