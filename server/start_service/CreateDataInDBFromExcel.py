import openpyxl


wb = openpyxl.load_workbook("C:\\Users\\erkin.mamadiyev\\PycharmProjects\\DavrBankDashboard\\server\\Просрочка на 23.10.23.xlsx")

sheets = wb.sheetnames
sh2 = wb['База']
print(type(sh2))