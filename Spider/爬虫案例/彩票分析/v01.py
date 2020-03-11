'''
随机生成一组双色球号码
'''
import random

def ball():
    ball_list = []
    # 随机生成6个红色球
    while 1:
        a = random.randint(1, 33)
        if a not in ball_list:
            ball_list.append(a)
        if len(ball_list) == 6:
            break

    ball_list.sort()
    # 随机h生成一个蓝色球
    ball_list.append(random.randint(1, 16))
    print(ball_list)

ball()