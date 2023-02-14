import pandas as pd
import helper
import os


def load_vpa_result_csv(vpa_res_path):
    """
    :return: 返回M1ta下variancePartition结果的dataframe
    """
    return helper.csv_to_data_frame(vpa_res_path, {'Unnamed: 0': 'gene_id_ENSG'})


def load_vst_exp_csv(vst_exp_path, name_list):
    """
    :return: 返回name_list中model对应的标准化表达矩阵的dataframe
    """
    # 遍历vst_exp_path下的所有文件，找到后缀名为_all_vst_dds.csv的文件
    # 再拼接name_list中的model名，找到对应的文件
    # 读取文件，返回dataframe
    df_data = pd.DataFrame()
    for root, dirs, files in os.walk(vst_exp_path):
        for name in files:
            if name.endswith('_all_vst_dds.csv'):
                for model in name_list:
                    if name.startswith(model):
                        tmp_df = helper.csv_to_data_frame(os.path.join(root, name), {'Unnamed: 0': 'gene_id_ENSG'})
                        tmp_df['model_type'] = model
                        df_data = pd.concat([df_data, tmp_df], ignore_index=True, join='outer')
    return df_data


def load_tsa_result_csv(tsa_res_path):
    """
    :return: 返回M1ta下TSA结果的dataframe
    """
    # 遍历 tsa_res_path 下名为 聚类结果 的文件夹
    # 读取前缀为gene_ID_的txt文件，其中每一行为一个gene_id_ENSG
    # 一个文件对应一个cluster，将cluster名和gene_id_ENSG存入字典，并转换为dataframe
    tsa_dict = {}
    cluster_path = os.path.join(tsa_res_path, '聚类结果')
    core_cluster_path = os.path.join(tsa_res_path, '核心基因集')
    for name in os.listdir(cluster_path):
        if name.startswith('geneID_'):
            cluster = name.replace('geneID_', '').replace('.txt', '')
            with open(os.path.join(cluster_path, name), 'r') as f:
                for line in f.readlines():
                    tsa_dict[line.strip()] = {'cluster': cluster, 'is_core': False}
    for name in os.listdir(core_cluster_path):
        if name.startswith('geneID_'):
            with open(os.path.join(core_cluster_path, name), 'r') as f:
                for line in f.readlines():
                    tsa_dict[line.strip()]['is_core'] = True
    # 将字典转换为dataframe
    df_data = pd.DataFrame.from_dict(tsa_dict, orient='index')
    # 重置index，原index为gene_id_ENSG
    df_data.reset_index(inplace=True)
    df_data.rename(columns={'index': 'gene_id_ENSG'}, inplace=True)
    return df_data


def load_tsa_enrichment_csv(tsa_enrichment_path):
    """
    :return: 返回M1ta下TSA富集结果的dataframe
    """
    df_data = pd.DataFrame()
    for file in os.listdir(tsa_enrichment_path):
        if file.startswith('gprofiler') and file.endswith('.csv'):
            cluster = file.replace('gprofiler_', '').replace('_core.csv', '')
            tmp_df = helper.csv_to_data_frame(os.path.join(tsa_enrichment_path, file),
                                              {})
            tmp_df['model_type'] = 'TSA'
            tmp_df['cluster'] = cluster
            if not tmp_df.empty:
                tmp_df = helper.check_is_represent_term(tmp_df, os.path.join(tsa_enrichment_path, file))
                df_data = pd.concat([df_data, tmp_df], ignore_index=True)
    return df_data


def load_wgcna_module_trait_csv(wgcna_module_trait_path):
    """
    :return: 返回M1ta下WGCNA 模块特征关系 的dataframe
    """
    correlation_value_file = 'heatmap_correlation_value.csv'
    p_value_file = 'heatmap_P_value.csv'

    # 将原dataframe的行名和列名转换为新dataframe的列x，y
    df_correlation_value = pd.read_csv(os.path.join(wgcna_module_trait_path, correlation_value_file), index_col=0)
    df_correlation_value.reset_index(inplace=True)
    df_correlation_value.rename(columns={'index': 'x'}, inplace=True)
    df_correlation_value = pd.melt(df_correlation_value, id_vars=['x'], var_name='y', value_name='correlation_value')
    # 同样处理P_value
    # 并将两个dataframe合并
    df_p_value = pd.read_csv(os.path.join(wgcna_module_trait_path, p_value_file), index_col=0)
    df_p_value.reset_index(inplace=True)
    df_p_value.rename(columns={'index': 'x'}, inplace=True)
    df_p_value = pd.melt(df_p_value, id_vars=['x'], var_name='y', value_name='p_value')
    df_correlation_value = pd.merge(df_correlation_value, df_p_value, on=['x', 'y'], how='outer')
    # 添加analyse列和 model_type列
    df_correlation_value['analyse'] = 'WGCNA'
    df_correlation_value['model_type'] = 'M1Ta'
    return df_correlation_value


def load_wgcna_module_info_csv(wgcna_module_info_file_path):
    """
    :return: 返回M1ta下WGCNA 模块信息 的dataframe
    """
    df_data = pd.read_csv(wgcna_module_info_file_path, index_col=0)
    df_data.reset_index(inplace=True)

    # 添加analyse列和 model_type列
    df_data['analyse'] = 'WGCNA'
    df_data['model_type'] = 'M1Ta'

    return df_data


def load_wgcna_gs_mm_csv(wgcna_gs_mm_file_path):
    """
    :return: 返回M1ta下WGCNA Gene-Trait Significance 和 Gene-Module Membership 的dataframe
    """
    df_data = pd.read_csv(wgcna_gs_mm_file_path, index_col=0)
    df_data.reset_index(inplace=True)
    df_data.rename(columns={'index': 'gene_id_ENSG'}, inplace=True)
    # 添加analyse列和 model_type列
    df_data['analyse'] = 'WGCNA'
    df_data['model_type'] = 'M1Ta'
    # 只导入gene_id_ENSG和module，前100行
    # 列名module 改为 mo_id_id
    df_data.rename(columns={'module': 'module_id'}, inplace=True)

    return df_data


def load_wgcna_enrichment_csv(wgcna_enrichment_path):
    """
    :return: 返回M1ta下WGCNA富集结果的dataframe
    """
    df_data = pd.DataFrame()
    for file in os.listdir(wgcna_enrichment_path):
        if file.startswith('gprofiler') and file.endswith('.csv'):
            module_id = file.replace('gprofiler_module_', '').replace('.csv', '')
            tmp_df = helper.csv_to_data_frame(os.path.join(wgcna_enrichment_path, file),
                                              {})
            tmp_df['model_type'] = 'M1Ta'
            tmp_df['module_id'] = module_id
            if not tmp_df.empty:
                tmp_df = helper.check_is_represent_term(tmp_df, os.path.join(wgcna_enrichment_path, file))
                df_data = pd.concat([df_data, tmp_df], ignore_index=True)
    return df_data


def load_wgcna_top30_network_csv(wgcna_top30_network_path):
    """
    :return: 返回M1ta下WGCNA top30网络的dataframe
    """
    df_data = pd.DataFrame()
    for file in os.listdir(wgcna_top30_network_path):
        if file.startswith('Cytoscape_edges_') and file.endswith('.csv'):
            module_id = file.replace('Cytoscape_edges_', '').replace('.csv', '')
            tmp_df = helper.csv_to_data_frame(os.path.join(wgcna_top30_network_path, file),
                                              {}, sep='\t')
            tmp_df['model_type'] = 'M1Ta'
            tmp_df['module_id'] = module_id
            if not tmp_df.empty:
                df_data = pd.concat([df_data, tmp_df], ignore_index=True)
    return df_data
