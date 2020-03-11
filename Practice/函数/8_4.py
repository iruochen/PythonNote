def print_models(a, b):
    while a:
        s = a.pop()
        print(s)
        b.append(s)

def show(b):
    for b1 in b:
        print(b1)

a = ['1', '2', '3', '4', '5']

b = []

# 切片法可以保留a的数据
print_models(a[:], b)
show(b)

print(a)
print(b)