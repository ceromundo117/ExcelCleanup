import pandas as pd
import openpyxl as op
from datetime import date

today = date.today()
today = today.strftime("%m_%d_%y")

print(
    '.xlsx is the standard excel file format please save your files in that format\n\nYour file name must be the '
    'exact same as the file name\nNo_spaces_only_underscores\n\nIf you have not done so already please drop your '
    'excel files in the program main file\n')


accutrac_export = input('Enter Accutrak Excel file name: ')
gs_excel = input('Enter Global Search Excel file name: ')

master = pd.read_excel(accutrac_export + '.xlsx', usecols=['Accutrac_Barcode', 'Major_Desc'])

master['Accutrac_Barcode'] = master['Accutrac_Barcode'] // 10
master = master.sort_values(by=['Accutrac_Barcode'])
master.to_excel(today + '.xlsx', index=False)
master2 = master[['Accutrac_Barcode']]

excel = pd.read_excel(gs_excel + '.xlsx', usecols=0, names=['Accutrac_Barcode'])
excel = excel.drop_duplicates('Accutrac_Barcode', keep='first', inplace=False)
excel2 = excel[['Accutrac_Barcode']]

combined_comparison = master2.append(excel2)

uniques = combined_comparison.drop_duplicates('Accutrac_Barcode', keep=False)
uniques.to_excel('Unique_Acts' + '.xlsx', index=False)

final_excel = uniques.append(excel2)
final_excel = final_excel.sort_values(by=['Accutrac_Barcode'])
final = final_excel.drop_duplicates('Accutrac_Barcode', keep=False, inplace=False)
final.to_excel('Title Application Excel ' + today + '.xlsx', index=False)