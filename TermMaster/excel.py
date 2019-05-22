# import xlsxwriter
#
# workbook = xlsxwriter.Workbook('Course_List.xlsx')
# worksheet = workbook.add_worksheet()
#
#
# alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#
# rows = 5
# cols = 5
#
# for row in range(rows):
#     for col in range(cols):
#         cell = alpha[col] + str(row+1)
#         print(cell)
#
# # worksheet.write('A1', 'Hello world')
# #
# # workbook.close()