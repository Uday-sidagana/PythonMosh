import openpyxl as xl
from openpyxl.chart import BarChart, Reference

def workbook(filename):

    wb= xl.load_workbook(filename)
    sheet =wb['Sheet1']
    cell = sheet.cell(1,1)
    cell = sheet['a1']
    print(cell.value)

    for i in range(1, sheet.max_row):
        cell = sheet.cell(i+1, 3)
        print(cell.value)

        correct= float(cell.value) * 0.9
        
        corrected_row= sheet.cell(i+1, 4)
        corrected_row.value = correct

    Values= Reference(sheet, min_row=2, max_row= sheet.max_row, 
            min_col=4, max_col=4)

    chart = BarChart()
    chart.add_data(Values)
    sheet.add_chart(chart, 'a5')

    wb.save(filename)

workbook('transactions.xlsx')



    