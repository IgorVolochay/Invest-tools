import tools.update_prices as price

if __name__ == '__main__':
    # Тестрование акций
    print(price.check_asset("SBER"))
    print(price.check_asset("VKCO"))
    print(price.check_asset("PIKK"))
    print(price.check_asset("ABRD"))
    print(price.check_asset("GAZP"))
    print(price.check_asset("POLY"))

    # Тестирование фондов
    print(price.check_asset("TRAI"))
    print(price.check_asset("TMOS"))
    print(price.check_asset("GOLD"))
    print(price.check_asset("AKGD"))
    print(price.check_asset("INGO"))
    print(price.check_asset("TCBR"))