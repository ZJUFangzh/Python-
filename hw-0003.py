# 需要安装redis
import redis

import string
import random


r = redis.Redis(host='127.0.0.1', port=7000, db=0)

chars = string.ascii_letters + string.digits

# 用random.sample 生成序列中的n个字符的片段，然后连起来


def generate(n, many=1, where=None):
    def getCode(n):
        return "".join(random.sample(chars, n))
    gene = [getCode(n) for i in range(many)]
    return gene


for x in range(201):
    codes = generate(20, 1)
    r.set(x, codes)
