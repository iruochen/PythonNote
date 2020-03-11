import itertools as its
import datetime

# 记录程序运行时间
start = datetime.datetime.now()
words = '1234567890'
# 生成密码的位置
# 生成8位密码
# 笛卡尔积
r = its.product(words, repeat=8)
dic = open(r"D:\Personal\Desktop\password.txt", 'a')
for i in r:
    dic.write(''.join(i))
    dic.write(''.join('\n'))

dic.close()
print("密码本生成完成")
end = datetime.datetime.now()
print("生成密码本一共用的时间: {}".format(end-start))
