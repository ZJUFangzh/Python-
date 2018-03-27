#coding: utf-8
# 用*号代替

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

    for i in words:
        if i in text:
            i_len = len(i)
            text = text.replace(i, "*" * i_len)
        else:
            pass
    print(text)

    if text == '0':
        break
