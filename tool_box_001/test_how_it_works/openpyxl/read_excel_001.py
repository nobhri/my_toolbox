# read_excel_001.py
import openpyxl
wb2 = openpyxl.load_workbook('test.xlsx')
print(wb2.sheetnames)