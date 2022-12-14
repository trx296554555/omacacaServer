import sqlite3
import time
import pandas as pd


def load_df_to_sqlite(data, connection, table_name):
    """
    :param data: 输入的数据，接受 DataFrame
    :param connection: 数据库连接
    :param table_name: 表名
    :return: 输出执行起止时间
    """
    print(f'{len(data)} 行数据被需要被导入')
    print(f"Now loading table {table_name} information, please wait...")
    start_time = time.time()

    data.to_sql(table_name, connection, if_exists='append', index=False, chunksize=10000)

    print(f"table {table_name} loaded, used time : {time.time() - start_time}")


def csv_to_data_frame(csv_file_path, col_dict, encoding='utf-8'):
    """
    :param csv_file_path: 需要读入的csv文件路径
    :param col_dict: 需要被修改的列名
    :param encoding: 读取csv的编码格式
    :return: 返回修改好列名的 dataFrame
    """

    data = pd.read_csv(csv_file_path, encoding=encoding)
    data.rename(columns=col_dict, inplace=True)
    # float 只保留8位
    # data = pd.concat([data.iloc[:, 0], data.iloc[:, 1:].applymap(lambda x: "%.8f" % x).applymap(float)], axis=1)

    return data
