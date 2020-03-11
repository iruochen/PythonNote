'''
search
'''
import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search("one123two456three78")
print(m.group())

# 参数表明搜查的起始范围
m = pattern.search("one123two456three78", 10, 40)
print(m.group())
