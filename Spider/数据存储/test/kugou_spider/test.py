a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 7, 9]

'''
要求：
1，4，7
2，5，8
3，6，9
'''

# for x, y, z in zip(a, b, c):
#     print(x, y, z)
#     print(type(zip(a, b, c)))


x = ['A', 'B', 'C']
y = [1, 2, 3]

try:
    pass
except:
    pass

s = dict(zip(x, y))
print(s)
print(type(s))

