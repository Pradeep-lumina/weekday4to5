import openpyxl

path = "D:/Fita class/Selenium Python/input.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.get_sheet_by_name("Sheet1")

for r in range(1, 6):
    for c in range(1,5):
        sheet.cell(row=r, column=c).value="Welcome"
    workbook.save(path)