import pandas as pd

from account.account_info import Account

stock_info_columns = ['StockCode', 'StockName', 'StockValue', 'StockNumber', 'StockAvailable',
                      'StockCurrentPrice', 'StockCost', 'StockProfitAndLost']

if __name__ == '__main__':
    account = Account()
    account.account_id = "0210078126"
    account.transfer = 80000.00

    print('* '*5 + 'First transfer 80000.00' + '* '*5)

    total_asset = account.get_total_asset()
    print(f'Total asset {total_asset}')

    print('* ' * 5 + 'Second transfer 20000.00' + '* ' * 5)

    account.transfer = 20000.00
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'account.account_id {account.account_id}')
    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info)

    print('B01 ' * 10 + ' Buy stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=10.00 ' + 'B ' * 10)

    account.buy(stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=10.00, buy_date="2021-08-26", trade_flag='B')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('B02 ' * 5 + ' Buy stock_code="SZ.600301", stock_name="LDGF", buy_number=1000, buy_price=15.00 ' + 'B ' * 5)

    account.buy(stock_code="SZ.600301", stock_name="LDGF", buy_number=1000, buy_price=15.00, buy_date="2021-08-26", trade_flag='B')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('B03 ' * 5 + ' Buy stock_code="SH.300666", stock_name="ZSZQ", buy_number=2000, buy_price=6.00 ' + 'B ' * 5)

    account.buy(stock_code="SH.300666", stock_name="ZSZQ", buy_number=2000, buy_price=6.00, buy_date="2021-08-26",
                trade_flag='B')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('B04 ' * 5 + ' Buy stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=14.00 ' + 'B ' * 5)

    account.buy(stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=14.00, buy_date="2021-08-26",
                trade_flag='B')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('B05 ' * 10 + ' Buy stock_code="SH.300666", stock_name="ZSZQ", buy_number=1000, buy_price=8.00 ' + 'B ' * 5)

    account.buy(stock_code="SH.300666", stock_name="ZSZQ", buy_number=1000, buy_price=8.00, buy_date="2021-08-26",
                trade_flag='B')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('B06 ' * 10 + ' Buy stock_code="SH.300666", stock_name="ZSZQ", buy_number=1000, buy_price=8.00 ' + 'B ' * 5)

    account.buy(stock_code="SH.300666", stock_name="ZSZQ", buy_number=1500, buy_price=7.00, buy_date="2021-08-26",
                trade_flag='B')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('S07 ' * 10 + ' Sale stock_code="SH.300666", stock_name="ZSZQ", sale_number=2000, sale_price=8.00 ' + 'B ' * 5)

    account.sale(stock_code="SH.300666", stock_name="ZSZQ", sale_number=2000, sale_price=8.00, sale_date="2021-08-26", trade_flag='S')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('S08 ' * 10 + ' Sale stock_code="SH.300666", stock_name="ZSZQ", sale_number=2500, sale_price=8.00 ' + 'S ' * 5)

    account.sale(stock_code="SH.300666", stock_name="ZSZQ", sale_number=2500, sale_price=10.00, sale_date="2021-08-26", trade_flag='S')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())

    print('S09 ' * 10 + ' Sale stock_code="SZ.600301", stock_name="ZSZQ", sale_number=2000, sale_price=14.00 ' + 'S ' * 5)

    account.sale(stock_code="SZ.600301", stock_name="ZSZQ", sale_number=5000, sale_price=14.00, sale_date="2021-08-26",
                 trade_flag='S')
    total_asset = account.get_total_asset()
    stock_value = account.get_stock_value()
    available_asset = account.get_available_asset()
    profit_and_loss = account.get_profit_and_loss()
    holding_stock_info = account.get_holding_stock()

    print(f'Total asset {total_asset}')
    print(f'Stock value {stock_value}')
    print(f'Stock available_asset {available_asset}')
    print(f'Stock profit_and_loss {profit_and_loss}')
    print(holding_stock_info.to_string())








