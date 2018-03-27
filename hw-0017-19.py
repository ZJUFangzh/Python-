import xlrd
import json
from lxml import etree


def read_exl(file_name):
    exl = xlrd.open_workbook(file_name)
    exl_sheet = exl.sheet_by_name('student')
    data = {}
    for i in range(exl_sheet.nrows):
        data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1:]

    return json.dumps(data, ensure_ascii=False)


def save_to_xml(data, new_file_name):
    root = etree.Element('root')
    students = etree.SubElement(root, 'students')
    students.append(etree.Comment(u"""学生信息表 "id" : [名字, 数学, 语文, 英文]"""))
    students.text = data

    students_xml = etree.ElementTree(root)
    students_xml.write(new_file_name, pretty_print=True,
                       encoding='utf-8')


content = read_exl('student.xls')
save_to_xml(content, 'student.xml')
