import os
import json
import xlwt

with open('student.txt', encoding='utf-8') as f:
    content = f.read()

d = json.loads(content)

file = xlwt.Workbook()
f_sheet = file.add_sheet('student')

for row, i in enumerate(d):
    f_sheet.write(row, 0, i)
    for col, j in enumerate(d[i]):
        f_sheet.write(row, col + 1, j)

file.save('student.xls')
