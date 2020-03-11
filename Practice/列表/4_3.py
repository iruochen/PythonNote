numbers = list(range(0, 5))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for i in range(1, 11):
    square = i ** 2
    squares.append(square)
print(squares)

num = []
for i in range(1, 11):
    num.append(i ** 2)
print(num)

print(min(num))
print(max(num))
print(sum(num))

num = [value ** 2 for value in range(1, 11)]
print(num)

for i in range(0, 21):
    print(i)

# nums =  [i for i in range(1, 1000001)]
# print(nums)

s = [i for i in range(1, 21, 2)]
print(s)

ss = [i for i in range(3, 31) if i % 3 == 0]
print(ss)
for i in ss:
    print(i)

sss = [i**3 for i in range(1, 11)]
print(sss)


