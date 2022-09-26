'''It checks date format of a excel sheet.
It checks each cell if its format is same as target_format or not.
Set parameters before you use it.
'''

import openpyxl

# parameters
file_path = 'test_datetime_format_01.xlsx'
sheet_name = "sheet_1"
# target_format = 'yyyy/mm/dd h:mm:ss'
target_format = 'yyyy"-"mm"-"dd' # NOTE: If you use "-", you need double quotes.

row_num_min = 2
row_num_max = 4
target_column = 1
# parameters end


# read .xlsx file
workbook_01 = openpyxl.load_workbook(file_path)

# get worksheet
worksheet_01 = workbook_01[sheet_name]


list_to_store_right_format_num = []
for row_num in range(row_num_min, row_num_max + 1):
    the_cell = worksheet_01.cell(row=row_num, column = target_column)
    # print(the_cell.number_format)
    if the_cell.number_format == target_format:
        list_to_store_right_format_num.append(the_cell)
    else:
        print(the_cell)# NOTE: It shows cells with unexpected format.

print(len(list_to_store_right_format_num))
    # NOTE: It counts number of cells with expected format