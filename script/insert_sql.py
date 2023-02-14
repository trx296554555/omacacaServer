import get_deg_df
import get_gene_df
import sqlite3
import helper
import statistical_deg_num

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

    # 数据元信息 导入表 MetaTable
    helper.load_df_to_sqlite(
        helper.csv_to_data_frame(r'D:\Lab\猕猴\可视化\Meta_info\Meta_info.csv', {}, encoding='gbk'),
        conn,
        'ltbm_metatable')
    # DEG ORA 结果导入表 DegTable
    helper.load_df_to_sqlite(get_deg_df.recursion_load_deg_csv(r'D:\Lab\猕猴\分析\转录组DEG\RES'), conn,
                             'ltbm_degtable')
    # DEG enrichment 导入表 DegEnrichmentTable
    helper.load_df_to_sqlite(get_deg_df.recursion_load_deg_enrichment_csv(r'D:\Lab\猕猴\分析\转录组DEG\GPF'),
                             conn, 'ltbm_degenrichmenttable')
    # DEG GSEA 结果导入表 GseaTable
    helper.load_df_to_sqlite(get_deg_df.recursion_load_gsea_enrichment_csv(r'D:\Lab\猕猴\分析\转录组DEG\GSEA'), conn,
                             'ltbm_gseaenrichmenttable')
    # DEG 数量统计结果导入表 DegHtmTable
    helper.load_df_to_sqlite(statistical_deg_num.get_htm_df(), conn, 'ltbm_deghtmtable')
    # DEG others 数量统计结果导入表 DegStkTable
    helper.load_df_to_sqlite(statistical_deg_num.get_stk_df(), conn, 'ltbm_degstktable')
    # M1Ta/M4Ta 的标准化表达矩阵 导入表 GeneVstExpTable
    helper.load_df_to_sqlite(get_gene_df.load_vst_exp_csv(r'D:\Lab\猕猴\分析\转录组DEG\RES', ['M1Ta', 'M4Ta']), conn,
                             'ltbm_genevstexptable')
    # VPA 结果导入表 VpaTable
    helper.load_df_to_sqlite(
        get_gene_df.load_vpa_result_csv(r'D:\Lab\猕猴\分析\VariancePartition\M1Ta\variancePartition.csv'), conn,
        'ltbm_vpatable')
    # TSA 结果导入表 TsaTable
    helper.load_df_to_sqlite(get_gene_df.load_tsa_result_csv(r'D:\Lab\猕猴\分析\Mfuzz时间序列分析\M1Ta'), conn,
                             'ltbm_tsatable')
    # TSA enrichment 导入表 TsaEnrichmentTable
    helper.load_df_to_sqlite(get_gene_df.load_tsa_enrichment_csv(r'D:\Lab\猕猴\分析\Mfuzz时间序列分析\M1Ta\富集结果'),
                             conn, 'ltbm_tsaenrichmenttable')
    # WGCNA module与Trait的关系导入表 WgcnaModuleTraitTable
    helper.load_df_to_sqlite(get_gene_df.load_wgcna_module_trait_csv(r'D:\Lab\猕猴\分析\WGCNA\M1Ta'), conn,
                             'ltbm_wgcnamoduletraittable')
    # WGCNA module info 总表导入表 WgcnaModuleInfoTable
    helper.load_df_to_sqlite(
        get_gene_df.load_wgcna_module_info_csv(r'D:\Lab\猕猴\分析\WGCNA\M1Ta\M1Ta_module_gene_info.csv'), conn,
        'ltbm_wgcnamoduleinfotable')
    # WGCNA Gene-Trait Significance 和 Gene-Module Membership 导入表 WgcnaGSMMTable
    helper.load_df_to_sqlite(get_gene_df.load_wgcna_gs_mm_csv(r'D:\Lab\猕猴\分析\WGCNA\M1Ta\module_gs_mm_info.csv'),
                             conn, 'ltbm_wgcnagsmmtable')
    # WGCNA module 的 enrichment 导入表 WgcnaEnrichmentTable
    helper.load_df_to_sqlite(get_gene_df.load_wgcna_enrichment_csv(r'D:\Lab\猕猴\分析\WGCNA\M1Ta\enrichment'), conn,
                             'ltbm_wgcnaenrichmenttable')
    # WGCNA module 的 top30 Network 导入表 WgcnaTop30NetworkTable
    helper.load_df_to_sqlite(
        get_gene_df.load_wgcna_top30_network_csv(r'D:\Lab\猕猴\分析\WGCNA\M1Ta\module_network_top30'), conn,
        'ltbm_wgcnatop30networktable')
    # cur.execute('SELECT * FROM getData_m1tavariancepartition')
    cursor.close()
