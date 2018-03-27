import os
import json
import xlwt

with open('city.txt', encoding='utf-8') as f:
    content = f.read()

d = json.loads(content)

file = xlwt.Workbook()
f_sheet = file.add_sheet('city')

for row, i in enumerate(d):
    f_sheet.write(row, 0, i)
    f_sheet.write(row, 1, d[i])
file.save('city.xls')
