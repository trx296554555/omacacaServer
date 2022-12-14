import get_deg_df
import sqlite3
import helper

if __name__ == '__main__':

    try:
        conn = sqlite3.connect(r'../omacaca.sqlite3')
        cursor = conn.cursor()
        print('数据库连接成功！')
        # cursor.execute("DELETE FROM ltbm_metatable")
        # cursor.execute("update sqlite_sequence set seq=0 where name='ltbm_metatable';")
        # conn.commit()
    except:
        print('数据库连接失败！')

    #  数据元信息 导入表 MetaTable
    helper.load_df_to_sqlite(helper.csv_to_data_frame(r'D:\lab\猕猴\可视化\Meta_info\Meta_info.csv', {}, encoding='gbk'),
                             conn,
                             'ltbm_metatable')
    # DEG ORA 结果导入表 DegTable
    helper.load_df_to_sqlite(get_deg_df.recursion_load_deg_csv(r'D:\lab\猕猴\分析\转录组DEG\RES'), conn,
                             'ltbm_degtable')
    # DEG enrichment 导入表 DegEnrichmentTable
    helper.load_df_to_sqlite(get_deg_df.recursion_load_deg_enrichment_csv(r'D:\lab\猕猴\分析\转录组DEG\GPF'),
                             conn,'ltbm_degenrichmenttable')


    # DEG GSEA 结果导入表 GseaTable

    # # M1Ta的 标准化表达矩阵 导入表 getData_m1taallvstexpression VariancePartition
    # load_df_to_sqlite(
    #     csv_to_data_frame(r'D:\Lab\猕猴\分析\VariancePartition\M1Ta\M1Ta_all_vst_dds.csv', {'Unnamed: 0': 'gene_id'}),
    #     conn, 'getData_m1taallvstexpression')
    # # M4Ta的 标准化表达矩阵 导入表 getData_m4taallvstexpression
    # load_df_to_sqlite(
    #     csv_to_data_frame(r'D:\Lab\猕猴\分析\VariancePartition\M4Ta\M4Ta_all_vst_dds.csv', {'Unnamed: 0': 'gene_id'}),
    #     conn, 'getData_m4taallvstexpression')

    # csv_to_data_frame(r'D:\Lab\猕猴\分析\VariancePartition\M1Ta\variancePartition.csv', {'Unnamed: 0': 'gene_id'})
    # cur.execute('SELECT * FROM getData_m1tavariancepartition')
    cursor.close()
