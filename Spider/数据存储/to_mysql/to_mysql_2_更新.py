import pymysql

# 数据库连接操作
db = pymysql.connect('localhost', 'root', 'root', 'test', 3306)
# 创建游标
cursor = db.cursor()

# SQL 更新
sql = "update ruochen set age = age - 1 where first_name = '%s'"%('ruo')
try:
    # 执行SQL 语句
    cursor.execute(sql)
    # 提交SQL数据库执行
    db.commit()
    print('执行成功')
except Exception as e:
    # 发生错误请回滚
    db.rollback()
    print('执行失败')
    print(e)
finally:
    # 关闭游标
    cursor.close()
    # 关闭数据库连接
    db.close()