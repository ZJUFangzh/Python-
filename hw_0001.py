'''第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''

import string
import random

chars = string.ascii_letters + string.digits

# 用random.sample 生成序列中的n个字符的片段，然后连起来


def generate(n, many=1, where=None):
    def getCode(n):
        return "".join(random.sample(chars, n))
    gene = [getCode(n) for i in range(many)]
    return gene


#print(generate(20, 200))
