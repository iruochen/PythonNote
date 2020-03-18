'''
Python连接MySQLdimo
1. 连接数据库 pymysql  Mysqldb
2. 获取记录
3. 增加记录
4. 修改记录
5. 删除记录
6. .....
'''
__author__ = "ruochen"
__time__ = "2020-3-17 23:35"

import pymysql

class MysqlDemo(object):
    # 设置数据库的连接参数，默认编码类型为utf-8，参数为字符串
    def __init__(self, host, username, password, dbname):
        self.conn = pymysql.connect(host, username, password, dbname, charset='utf8')
        self.cursor = self.conn.cursor()

    # 获取所有数据, 此处传值为sql语句
    def get_all(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            return False

    # 获取单条数据
    def get_one(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            return False

    # 插入一条数据,
    def insert(self, data):
        pass

    # 更新记录  tableName  data(字典)  restriction(str)
    def update(self, table_name, data, restriction):
        data_str = ''
        for item in data.items():
            data_str += '{}="{}",'.format(item[0], item[1])
        values = data_str[:-1]
        sql = 'update {} set {} where {}'.format(table_name, values, restriction)

        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False
