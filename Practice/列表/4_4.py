s = [i for i in range(0, 5)]
print(s)
print(s[4::5])
print(s[0:3])
print(s[1:4])
print(s[:4])
print(s[1:])
print(s[-3:])

print(s)
ss = s
print(ss)
print(id(s))
print(id(ss))
s.append("9")
# ss.append("0")
print(s)
print(ss)

sss = s[:]
print(sss)
print(id(sss))
sss.append("10")
print(sss)
print(s)
