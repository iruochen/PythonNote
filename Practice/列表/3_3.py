num = ["5", "2", "1", "3", "4"]
print(num)

# 顺序
num.sort()
print(num)

# 倒序
num.sort(reverse=True)
print(num)

# 临时排序
print(sorted(num))
print(num)

# 反转
num.reverse()
print(num)
num.reverse()
print(num)
print(num[-1])

# 确定列表长度
print(len(num))

a = [i for i in range(1, 6)]
b = [i for i in range(6, 11)]
print(a)
print(b)
a.extend(b)
print(a)
s = a.count(1)
print(s)