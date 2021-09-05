import pandas as pd
from data.daily_data import DataAPI


data_file_path = 'E:\\PycharmProjects\\operationalresearch\\data_file'
csv_file = '600999.csv'



if __name__ == '__main__':
    data_api = DataAPI()
    data_api.get_df_data_from_cvs(csv_file)
    df_last_row = data_api.get_data_tail(1)
    print(df_last_row.values)
    for row in data_api.get_stock_data_except_last_row():
        trade_date = str(row['trade_date'])
        daily_open = row['open']
        daily_close = row['close']
        daily_ma20 = row['ma30']

        print(row.values)


