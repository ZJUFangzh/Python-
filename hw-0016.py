import os
import json
import xlwt

with open('number.txt', 'r', encoding='utf-8') as f:
    content = f.read()

d = json.loads(content)

file = xlwt.Workbook()
f_sheet = file.add_sheet('number')

for row, i in enumerate(d):
    for col, j in enumerate(i):
        f_sheet.write(row, col, j)

file.save('number.xls')
