'''
mongoDB：非关系型数据库
mongoDB属于更加适合爬虫的数据库
mongoDBs是一个基于分布式文件存储的数据库，由c++编写
主要为web应用提供可扩展的高性能数据存储解决方案
默认端口号：27017


概念说明：
SQL：           MongoDB：         说明
database        database          数据库
table           collection        表/集合
row             document          行/文档
column          field             字段/域
index           index             索引
primary         primary           主键/_id为主键

安装mongoDB
    sudo apt-get install mongodb

如何python操作mongodb
    pip install pymongo

'''
# 导入需要的包pymongo
import pymongo

# 连接mongodb数据库, 默认连接本地
# client = pymongo.MongoClient()
# client = pymongo.MongoClient('127.0.0.1', 27017)
client = pymongo.MongoClient('mongodb://127.0.0.1:27017')

# 获取到数据库，连接数据库