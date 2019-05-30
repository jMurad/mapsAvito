import xlrd



path = r"C:\Users\yahyaevml\Desktop\for Muslim.xlsx"

wb = xlrd.open_workbook(path)
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(1, 1))

# Extracting number of rows
print(sheet.nrows)

