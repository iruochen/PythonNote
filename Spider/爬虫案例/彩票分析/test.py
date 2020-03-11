from collections import Counter

l = [4, 6, 2, 7, 9, 4, 6, 6, 4, 6, 9, 1]

s = Counter(l)
print(s)

ss = sorted(s.items(), key=lambda x:x[1], reverse=True)
print(ss)

ss1 = ss[0:3]
print(ss1)

ss2 = ss[3:6]
print(ss2)

sss = list(map(lambda x:x[0], ss1))
print(sss)

sss.sort()
print(sss)
