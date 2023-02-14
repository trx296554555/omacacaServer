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


def csv_to_data_frame(csv_file_path, col_dict, encoding='utf-8', sep=','):
    """
    :param csv_file_path: 需要读入的csv文件路径
    :param col_dict: 需要被修改的列名
    :param encoding: 读取csv的编码格式
    :param sep: csv文件的分隔符
    :return: 返回修改好列名的 dataFrame
    """

    data = pd.read_csv(csv_file_path, encoding=encoding, sep=sep)
    data.rename(columns=col_dict, inplace=True)
    # float 只保留8位
    # data = pd.concat([data.iloc[:, 0], data.iloc[:, 1:].applymap(lambda x: "%.8f" % x).applymap(float)], axis=1)

    return data


def check_is_represent_term(df, same_path, method='ora'):
    """
    获取df相同目录下的wsc和ap文件中的represent term，并将df中的term与wsc和ap中的represent term进行比对，有则标记为true，无则false
    :param df: 需要检查的dataframe
    :param same_path: 需要检查的term
    :param method: 检查的方法，ora或者gsea
    :return: 返回df
    """
    # 获取represent term
    wsc_represent_term = []
    ap_represent_term = []
    try:
        if method == 'ora':
            wsc_file = same_path.replace('.csv', '_wsc_representatives.txt')
            ap_file = same_path.replace('.csv', '_ap_representatives.txt')
        elif method == 'gsea':
            wsc_file = same_path.replace('_GSEA', '').replace('.csv', '_wsc_representatives.txt')
            ap_file = same_path.replace('_GSEA', '').replace('.csv', '_ap_representatives.txt')

        with open(wsc_file, 'r') as f:
            for line in f.readlines():
                wsc_represent_term.append(line.strip())
        with open(ap_file, 'r') as f:
            for line in f.readlines():
                ap_represent_term.append(line.strip())

    except FileNotFoundError:
        print(f'找不到{same_path}下的wsc和ap的represent term文件')
    # 检查df中的term是否在represent term中
    df['represent_term_wsc'] = df['term_id'].apply(lambda x: True if x in wsc_represent_term else False)
    df['represent_term_ap'] = df['term_id'].apply(lambda x: True if x in ap_represent_term else False)
    # 计算rich factor
    if method == 'ora':
        df['rich_factor'] = df['intersection_size'] / df['term_size']
    else:
        df['rich_factor'] = df['leading_edge_number'] / df['setSize']

    return df
