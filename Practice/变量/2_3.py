'''
字符串的处理
'''
# 大小写处理
name = "ada lovelace"
print(name.title())

name = "Ada LoVelace"
print(name.upper())
print(name.lower())

# 字符串拼接
first_name = "hello"
last_name = "python"
full_name = first_name + " " + last_name
print(full_name)

print(full_name.title() + "!")

print("Python")
print("\tPython")


# 空白清除
message = "python "
print(message)

message = message.rstrip()
print(message)

message = " python"
print(message)

message = message.lstrip()
print(message)

message = " python "
print(message)

message = message.strip()
print(message)

# 练习
name = "ruo chen"
print(name.title())
print(name.upper())
print(name.lower())

