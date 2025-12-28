# n=int(input("Enter Num: "))
# x=0
# y=1
# z=0
# while (z<=n):
#     print(z)
#     x=y
#     y=z
#     z=x+y
# print(z)

import openpyxl

book = openpyxl.load_workbook("C:\\Users\Akhilesh\\Desktop\\ETL_Testing_Test_Cases.xlsx")
sheet= book.active
print(sheet)