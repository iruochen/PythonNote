from pymongo import MongoClient

class MongoAPI(object):
    def __init__(self, db_ip, db_port, db_name, collection_name):
        self.db_ip = db_ip
        self.db_port = db_port
        self.db_name = db_name
        self.collection_name = collection_name
        self.coon = MongoClient(host=self.db_ip, port=self.db_port)

        self.db = self.coon[self.db_name]
        self.collection = self.db[self.collection_name]

    # 获取一条数据
    def get_one(self, query):
        return self.collection.find_one(query, property={'_id': False})

    # 获取多条数据
    def get_all(self, query):
        return self.collection.find(query)

    # 添加数据
    def add(self, kv_dict):
        return self.collection.insert(kv_dict)

    # 删除数据
    def delete(self, query):
        return self.collection.delete_many(query)

    # 查看集合中是否包含满足条件的数据，如果有则返回True，没有则新建
    def check(self, query):
        ret = self.collection.find_one(query)
        return ret != None
    def update(self, query, kv_dict):
        self.collection.update_one(query, {'$set': kv_dict}, upsert=True)