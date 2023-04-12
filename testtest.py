import openpyxl

# 打开Excel文件
workbook = openpyxl.load_workbook('/Users/wt/Documents/Test.xlsx')

# 选择第一个工作表
sheet = workbook.active

# 遍历A和B列，将它们的值相加，并将结果写入C列
for row in sheet.iter_rows(min_row=2, min_col=1, max_col=3):
    a = row[0].value
    b = row[1].value
    c = a + b
    row[2].value = c

# 保存Excel文件
workbook.save('/Users/wt/Documents/Test1.xlsx')