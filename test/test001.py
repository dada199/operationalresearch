import pandas as pd


stock_info_columns = ['StockCode', 'StockName', 'StockValue', 'StockNumber', 'StockAvailable',
                      'StockCurrentPrice', 'StockCost', 'StockProfitAndLost']

if __name__ == '__main__':
    buy_stock_data01 = [
        {
            'StockCode': "6003001",
            'StockName': "stock_name",
            'StockValue': 1000 * 50.35,
            'StockNumber': 1000,
            'StockAvailable': 1000,
            'StockCurrentPrice': 50.35,
            'StockCost': 50.35,
            'StockProfitAndLost': 0
        }]
    buy_stock_data02 = [
        {'StockCode': "300225",
         'StockName': "stock_name001",
         'StockValue': 1000 * 6.3,
         'StockNumber': 1000,
         'StockAvailable': 1000,
         'StockCurrentPrice': 6.3,
         'StockCost': 6.3,
         'StockProfitAndLost': 0
         }]
    buy_stock_data03 = [
        {'StockCode': "300225",
         'StockName': "stock_name001",
         'StockValue': 5000 * 8.0,
         'StockNumber': 5000,
         'StockAvailable': 5000,
         'StockCurrentPrice': 10.0,
         'StockCost': 10.0,
         'StockProfitAndLost': 0
         }]

    df1 = pd.DataFrame(data=buy_stock_data01, columns=stock_info_columns)
    df1 = df1.append(buy_stock_data02, ignore_index=True)

    df_new_line = pd.DataFrame(buy_stock_data03, index=[-1])

    print(df1)
    print(df_new_line)

    print(df1[df1['StockCode'] == "300225"].index.tolist())
    print(df_new_line[df_new_line['StockCode'] == "300225"].index.tolist())

    print(df_new_line.at[df_new_line[df_new_line['StockCode'] == "300225"].index.tolist()[0], 'StockValue'])

    print(df_new_line.at[-1, 'StockValue'])




