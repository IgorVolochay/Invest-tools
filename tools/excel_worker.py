import openpyxl

def get_tikker(path):
    workbook = openpyxl.load_workbook(path)
    workbook._active_sheet_index = 1 # Выбрать номер листа с данными
    sheet_obj = workbook.active()

    all_ticker = set()
    for index in range(2, sheet_obj.max_row + 1):
        ticker = sheet_obj.cell(index, 2).value
        all_ticker.add(ticker)

    return all_ticker