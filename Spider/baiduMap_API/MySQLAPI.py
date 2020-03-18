import pymysql

db = pymysql.connect('127.0.0.1', 'root', 'root', 'BaiduMap')
cursor = db.cursor()

# 创建city表
# sql = '''
# CREATE TABLE if not exists city(
# id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# city VARCHAR(200) NOT NULL,
# park VARCHAR(200) NOT NULL,
# location_lat FLOAT,
# location_lng FLOAT,
# address VARCHAR(200),
# street_id VARCHAR(200),
# uid VARCHAR(200),
# create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
# '''
# cursor.execute(sql)

#****************************************************************#
# 创建parkInfo表
# sql = '''
# CREATE TABLE if not exists parkInfo(
# id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# uid VARCHAR(200),
# street_id VARCHAR(200),
# park_name VARCHAR(200),
# address VARCHAR(200),
# shop_hours VARCHAR(200),
# detail_url VARCHAR(200),
# content_tag VARCHAR(300),
# create_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
# '''
# cursor.execute(sql)


class Sql(object):
    @classmethod
    def insert_city(cls, city, park, location_lat, location_lng, address, street_id, uid):
        sql = 'insert into city(city, park, location_lat, location_lng, address, street_id, uid)' \
              ' VALUES (%(city)s,%(park)s,%(location_lat)s,%(location_lng)s,%(address)s,%(street_id)s,%(uid)s)'

        value = {
            'city': city,
            'park': park,
            'location_lat': location_lat,
            'location_lng': location_lng,
            'address': address,
            'street_id': street_id,
            'uid': uid,
        }

        try:
            cursor.execute(sql, value)
            db.commit()
            print('插入成功')
        except Exception as e:
            print('插入失败～', e)
            db.rollback()

    'uid, street_id, park_name, address, shop_hours, detail_url, content_tag'
    @classmethod
    def insert_park(cls, uid, street_id, park_name, address, shop_hours, detail_url, content_tag):
        sql = 'insert into parkInfo(uid, street_id, park_name, address, shop_hours, detail_url, content_tag)' \
              ' VALUES (%(uid)s,%(street_id)s,%(park_name)s,%(address)s,%(shop_hours)s,%(detail_url)s,%(content_tag)s)'

        value = {
            'uid': uid,
            'street_id': street_id,
            'park_name': park_name,
            'address': address,
            'shop_hours': shop_hours,
            'detail_url': detail_url,
            'content_tag': content_tag,
        }

        try:
            cursor.execute(sql, value)
            db.commit()
            print('插入成功')
        except Exception as e:
            print('插入失败～', e)
            db.rollback()


    # 读取city表的uid号
    @classmethod
    def read_city(cls):
        sql = 'SELECT uid from city where id > 0;'
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        return results