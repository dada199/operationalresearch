import pandas as pd


from data.daily_data import DataAPI


class Strategy:

    def __init__(self, account, data_api):
        self.account = account
        self.data_api = data_api

    def strategy_get_account(self):
        return self.account.get_holding_stock()

    def ma20_strategy(self):
        # self.data_api.get_df_data_from_cvs()

        df_last_row = self.data_api.get_data_tail(1)
        y_open = df_last_row.at[0, 'open']
        y_close = df_last_row.at[0, 'close']
        y_ma20 = df_last_row.at[0, 'ma20']

        for row in self.data_api.get_stock_data_except_last_row():
            ts_code = str(row['ts_code'])
            trade_date = str(row['trade_date'])
            today_open = row['open']
            today_close = row['close']
            today_ma20 = row['ma20']

            # 未持仓
            if max(y_open, y_close) <= y_ma20:
                if today_close > today_ma20:
                    self.account.buy(stock_code=ts_code, stock_name="LDGF", buy_number=1000, buy_price=today_close, buy_date=trade_date)

                y_open = today_open
                y_close = today_close

                continue

            # 持仓
            if min(y_open, y_close) >= y_ma20:
                if today_close < today_ma20:
                    self.account.sale(stock_code=ts_code, stock_name="LDGF", sale_number=1000, sale_price=today_close, sale_date=trade_date)
                y_close = today_close
                y_open = today_open

                continue

            # 未持仓
            if y_close < y_ma20 < y_open:
                if today_close > 20:
                    self.account.buy(stock_code=ts_code, stock_name="LDGF", buy_number=1000, buy_price=today_close, buy_date=trade_date)
                y_close = today_close
                y_open = today_open

                continue

            # 持仓
            if y_open < y_ma20 < y_close:
                if today_close < 20:
                    self.account.sale(stock_code=ts_code, stock_name="LDGF", sale_number=1000, sale_price=today_close, sale_date=trade_date)
                y_close = today_close
                y_open = today_open

                continue


