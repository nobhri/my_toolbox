import openpyxl

# read .xlsx file
workbook_01 = openpyxl.load_workbook('test.xlsx') # returns list
print(workbook_01.sheetnames)

# get worksheet
worksheet_01 = workbook_01["sheet1"]

# get cell value pattern 1
cell_01 = worksheet_01['A1']
print(cell_01.value)


# get cell value pattern 2
cell_02 = worksheet_01.cell(row=4, column=2)
print(cell_02.value)