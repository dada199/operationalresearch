import pandas as pd

from account.account_info import Account

stock_info_columns = ['StockCode', 'StockName', 'StockValue', 'StockNumber', 'StockAvailable',
                      'StockCurrentPrice', 'StockCost', 'StockProfitAndLost']

if __name__ == '__main__':
    account = Account()
    account.account_id = "0210078126"
    account.transfer = 124000.00

    print('* '*5 + 'First transfer 80000.00' + '* '*5)
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

    account.buy(stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=15.50, buy_date="2021-08-26",
                trade_flag='B')
    account.buy(stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=15.50, buy_date="2021-08-26",
                trade_flag='B')
    account.buy(stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=15.50, buy_date="2021-08-26",
                trade_flag='B')
    account.buy(stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=15.50, buy_date="2021-08-26",
                trade_flag='B')

    print('B01 ' * 10 + ' Buy stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=10.00 ' + 'B ' * 10)
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

    account.sale(stock_code="SZ.600301", stock_name="ZSZQ", sale_number=2000, sale_price=15.50, sale_date="2021-08-26",
                 trade_flag='S')
    account.sale(stock_code="SZ.600301", stock_name="ZSZQ", sale_number=2000, sale_price=15.50, sale_date="2021-08-26",
                 trade_flag='S')
    account.sale(stock_code="SZ.600301", stock_name="ZSZQ", sale_number=2000, sale_price=15.50, sale_date="2021-08-26",
                 trade_flag='S')
    account.sale(stock_code="SZ.600301", stock_name="ZSZQ", sale_number=1000, sale_price=30.50, sale_date="2021-08-26",
                 trade_flag='S')

    print('S02 ' * 10 + ' Buy stock_code="SZ.600301", stock_name="LDGF", buy_number=2000, buy_price=10.00 ' + 'S ' * 10)
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







