import pandas as pd
import numpy as np
import time
import os
import logging

data_file_path = 'E:\\PycharmProjects\\operationalresearch\\data_file'
csv_file = '600999.csv'

logger = logging.getLogger(__name__)


class DataAPI:

    def __init__(self, file_name):
        self._file_name = file_name

    def get_stock_daily(self):
        full_path = os.path.join(data_file_path, self._file_name)
        if not os.path.exists(full_path):
            logger.warning(f'There is no file {self._file_name}')
            return
        logger.info(f'There is no file {self._file_name}')

        try:
            stock_data = pd.read_csv(full_path, encoding='utf-8')

            for index, values in stock_data[::-1].iterrows():
                # print(values['trade_date'], type(str(values['trade_date'])), values['open'], type(values['open']))
                yield values
                # time.sleep(0.05)
        except IOError:
            logger.info(f'There is no file {self._file_name}')

