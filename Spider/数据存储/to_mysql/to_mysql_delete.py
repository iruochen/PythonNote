import pymysql

db = pymysql.connect('localhost', 'root', 'root', 'test', 3306)
cursor = db.cursor()
sql = 'delete from ruochen where first_name = "%s"' % ('ruo')
try:
    cursor.execute(sql)
    db.commit()
    print('执行成功')
except Exception as e:
    db.rollback()
    print('执行失败')
    print(e)
finally:
    cursor.close()
    db.close()