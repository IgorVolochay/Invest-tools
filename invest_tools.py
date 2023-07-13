import tools.update_prices as price
import tools.excel_worker as excel

if __name__ == '__main__':
    path_workbook = "assets.xlsx" # Выбрать путь до книги Excel

    tickers_in_book = excel.get_tikker(path_workbook)

    current_price = dict()
    for ticker in tickers_in_book:
        current_price[ticker] = price.check_asset(ticker)

    print(current_price)