'''
数据存储之MySQL
Ubuntu环境安装MySQL
    sudo apt-get update
    sudo apt-get install mysql-server
    sudo apt-get install mysql-client
    sudo apt-get install libmysqlclient-dev

Linux rhel7 下MySQL安装：
https://www.cnblogs.com/guozhiping/p/7684134.html

MySQL数据库远程连通
    1. 修改 /etc/mysql/my.conf
        找到 bind-address = 127.0.0.1 这一行，将这一行注释
        或者：将这一行改为 bind-address = 0.0.0.0

    2. 让root用户支持远程连接MySQL数据库
        mysql -u root -p密码
        grant all privileges on *.* to root@'%' identified by 'password' with grant option;
        flush privileges

    3. rhel7 中防火墙允许mysql五福通过
        firewall -cmd --permanent --add-service=mysql
        firewall -cmd --reload


Python操作mysql (pymysql)
    pip install pymysql
'''

# python 操作mysql 创建数据表
import pymysql
# try:
#     # 获取一个数据库连接，注意：如果是utf8类型，需要定制数据库
#     # 打开数据库连接
#     '''
#     host='127.0.0.1',  # 数据库服务器地址
#     user='root',       # 登陆数据库用户
#     password='root',   # 数据库用户密码
#     db='test',         # 所连接的数据库名
#     port=3306          # 数据库端口，mysql默认3306
#     '''
#     basedata = {
#         'host': 'localhost',
#         'user': 'root',
#         'password': 'root',
#         'db': 'test',
#         'port': 3306,
#         'charset': 'utf8'
#     }
#     db = pymysql.connect(**basedata)
#     # 创建游标，对数据库进行操作，使用cursor()方法
#     cursor = db.cursor()
#     # 使用execute() 执行sql语句
#     cursor.execute('drop tables if exists ruochen')
#     # 使用预处理语句创建表
#     sql = '''create table ruochen(
#             first_name char(20) not null,
#             last_name char(20),
#             age int,
#             sex char(1),
#             income float
#             )'''
#     cursor.execute(sql)
#
#     # commit 修改
#     db.commit()
#     # 关闭游标
#     cursor.close()
#
#     # 关闭链接
#     db.close()
#     print('添加成功')
# except:
#     print('创建失败 ～ ～')




# # 数据库插入操作
# db = pymysql.connect('localhost', 'root', 'root', 'test')
# # 利用cursor()创建游标对象
# cursor = db.cursor()
# # sql语句执行
# # sql = 'insert into ruochen(first_name, last_name, age, sex, income) values ("ruo", "chen", 18, "M", 2000), ("lao", "wang", 20, "M", "1000")'
# # 为了防止sql注入
# sql = 'insert into ruochen (first_name, last_name, age, sex, income) values ("%s", "%s", "%d", "%c", "%s")' \
#         % ('ruo', 'chen', 18, 'M', '2000.3')
#
# # sql = 'insert into ruochen (first_name, last_name, age, sex, income) values (%s, %s, %s, %c, %s)'
#
# try:
#     # 执行sql语句
#     # cursor.execute(sql, ('ruo', 'chen', 18, 'M', 2000.3))
#     cursor.execute(sql)
#     # 提交执行
#     db.commit()
#     print('执行成功!')
# except Exception as e:
#     # 发生异常
#     print(e)
#     db.rollback()
#     print('执行失败!')
# finally:
#     # 关闭游标
#     cursor.close()
#     # 关闭数据库连接
#     db.close()




# 数据库查询操作
try:
    db = pymysql.connect('localhost', 'root', 'root', 'test', 3306)
    cursor = db.cursor()
    cursor.execute('select * from ruochen')
    datas = cursor.fetchall()
    for data in datas:
        print(data)
    cursor.close()
    db.close()
except Exception as e:
    print('查询失败!')
    print(e)


'''
fetchall(): 接收全部返回结果
fetchone(): 获取下一个查询结果集
rowcount: 只读属性，返回执行语句影响的行数
'''