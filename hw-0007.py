import os
import string
import re

PATH = r'D:\Python-trying\Python-trying'
os.chdir(PATH)
annotation = r'^\#.'
space = r'^\s+$'


def getCounter(source):
    code_lines = 0
    comm_lines = 0
    space_lines = 0
    with open(source) as f:
        for line in f.readlines():
            if re.match(space, line):
                space_lines += 1
            elif re.match(annotation, line):
                comm_lines += 1
            else:
                code_lines += 1

    list = [code_lines, comm_lines, space_lines]
    return list


def conde_lines_count(PATH):
    total_list = [0, 0, 0]
    for i in os.listdir(os.getcwd()):
        if os.path.splitext(i)[1] == '.py':
            total_list = list(
                map(lambda x: x[0] + x[1], zip(total_list, getCounter(i))))
    return total_list


print(conde_lines_count(PATH))
