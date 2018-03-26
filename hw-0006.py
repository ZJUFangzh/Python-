# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
# 假设内容都是英文，请统计出你认为每篇日记最重要的词。

import re
import os
from collections import Counter

PATH = r'F:\123'


def getCounter(source):
    with open(source) as f:
        data = f.read()
    data = data.lower()
    datalist = re.split(r'[\s]+', data)
    return Counter(datalist)


def run(PATH):
    os.chdir(PATH)
    total_counter = Counter()
    # 遍历该目录下的txt文件
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.txt':
            total_counter += getCounter(i)
    return total_counter.most_common()


dic = run(PATH)
for i in range(len(dic)):
    print('%15s  ---->   %3s' % (dic[i][0], dic[i][1]))
