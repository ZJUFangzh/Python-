# 将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
# https://blog.csdn.net/daphne566/article/details/54767080
import mysql.connector

import random
import string


chars = string.ascii_letters + string.digits


def generate(n, many=1, where=None):
    def getCode(n):
        return "".join(random.sample(chars, n))
    gene = [getCode(n) for i in range(many)]
    return gene


codes = generate(20, 200)

# 链接数据库
conn = mysql.connector.connect(user='root', password='', database='test')

# 创建游标
cursor = conn.cursor()

# 在test中创建一个abc的库
cursor.execute('create table abc (name varchar(20))')


for code in codes:
    cursor.execute('insert into abc (name) values ( %s)', [code])
