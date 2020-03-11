'''
python对json文件操作分为编码与解码
dumps    字符串
dump     json对象  可以通过fp文件流写入文件

解码：
    load
    loads
'''

import json

str = "[{'username': 'ruochen', 'age': '18'}]"
# print(type(str))
json_str = json.dumps(str, ensure_ascii=False)
print(json_str)
print(type(json_str))
new_str = json.loads(json_str)
print(new_str)
print(type(new_str))
