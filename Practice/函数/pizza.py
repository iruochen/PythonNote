'''
传递任意数量的参数
'''

# 创建一个空元组
def make_pizza(*toppings):
    for topping in toppings:
        print("\n- " + topping)