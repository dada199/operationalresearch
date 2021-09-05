import pandas as pd

from account.account_info import Account
from data.daily_data import DataAPI

stock_info_columns = ['StockCode', 'StockName', 'StockValue', 'StockNumber', 'StockAvailable',
                      'StockCurrentPrice', 'StockCost', 'StockProfitAndLost']

# account = Account()
# account.account_id = "0210078126"
# account.transfer = 80000.00


def ma20_strategy(csv_file, account):
    data_api = DataAPI(csv_file)

    # 未持仓
    if max(y_open, y_close) <= y_ma20:
        if today_close > today_ma20:
            account.buy()
        y_close = today_close
        y_open = today_open

        return

    # 持仓
    if min(y_open, y_close) >= y_ma20:
        if today_close < today_ma20:
            account.sale()
        y_close = today_close
        y_open = today_open

        return

    # 未持仓
    if y_close < y_ma20 < y_open:
        if today_close > 20:
            account.buy()
        y_close = today_close
        y_open = today_open

        return

    # 持仓
    if y_open < y_ma20 < y_close:
        if today_close < 20:
            account.sale()
        y_close = today_close
        y_open = today_open

        return










