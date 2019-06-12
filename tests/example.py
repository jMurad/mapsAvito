import xlrd


path = r"trash/data.xlsx"

wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)

# print(sheet.row_values(0))
baza = sheet.col_values(0)
print(baza[0])

