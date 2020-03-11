num = ["1", "2", "3"]
num[0] = "2"
print(num)

# 添加元素
num.append("4")
print(num)

num = []
for i in range(0, 4):
    num.append(i)
print(num)

# 插入元素
num.insert(1, 4)
print(num)

# 删除
del num[1]
print(num)

poped_num = num.pop()
print(num)
print(poped_num)

poped_num = num.pop(0)
print(num)
print(poped_num)

num.remove(1)
print(num)