# 敏感词检测
#coding: utf-8

path = 'd:/Python-trying/Python-trying/123.txt'


def filtered_words(path):
    words = []
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    return words


words = filtered_words(path)
while True:
    text = input("content:").strip()
    if text in words:
        print('Freedom')
    else:
        print('Human Rights')
