import insert_degtable
import sqlite3
import helper

if __name__ == '__main__':

    try:
        conn = sqlite3.connect(r'../omacaca.sqlite3')
        cursor = conn.cursor()
        print('数据库连接成功！')
    except:
        print('数据库连接失败！')

    # VariancePartition 结果导入表 DegTable
    helper.load_df_to_sqlite(insert_degtable.load_csv_from_local(r'D:\Lab\猕猴\分析\RES'), conn, 'ltbm_degtable')


    # # M1Ta的 标准化表达矩阵 导入表 getData_m1taallvstexpression
    # load_df_to_sqlite(
    #     csv_to_data_frame(r'D:\Lab\猕猴\分析\VariancePartition\M1Ta\M1Ta_all_vst_dds.csv', {'Unnamed: 0': 'gene_id'}),
    #     conn, 'getData_m1taallvstexpression')
    # # M4Ta的 标准化表达矩阵 导入表 getData_m4taallvstexpression
    # load_df_to_sqlite(
    #     csv_to_data_frame(r'D:\Lab\猕猴\分析\VariancePartition\M4Ta\M4Ta_all_vst_dds.csv', {'Unnamed: 0': 'gene_id'}),
    #     conn, 'getData_m4taallvstexpression')

    # csv_to_data_frame(r'D:\Lab\猕猴\分析\VariancePartition\M1Ta\variancePartition.csv', {'Unnamed: 0': 'gene_id'})
    # cur.execute('SELECT * FROM getData_m1tavariancepartition')
