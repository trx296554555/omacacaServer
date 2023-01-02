import pandas as pd
import helper
import os


def recursion_load_deg_csv(res_path):
    """
    :param res_path: 需要读入的DEG结果路径，如：E:\\RES
    :return: 返回拼接好的包含所有model结果的dataframe
    """
    root_value = 'logFC1_padj0.05'
    df_data = pd.DataFrame()
    if os.path.isdir(res_path):
        for model in os.listdir(res_path):
            model_name = os.path.basename(model)
            for table_dir in os.listdir(os.path.join(res_path, model, root_value)):
                if os.path.isdir(os.path.join(res_path, model, root_value, table_dir)):
                    print('Loading ', model, ':', table_dir)
                    comp1_name = table_dir.strip().split('_')[0]
                    comp2_name = table_dir.strip().split('_')[2]
                    csv_file = os.path.join(res_path, model, root_value, table_dir,
                                            model_name + '_' + table_dir + '.csv')
                    tmp_df = helper.csv_to_data_frame(csv_file, {'Unnamed: 0': 'gene_id_ENSG'})
                    tmp_df['model_type'] = model
                    tmp_df['comp1'] = comp1_name
                    tmp_df['comp2'] = comp2_name
                    df_data = pd.concat([df_data, tmp_df], ignore_index=True)
    else:
        print(f"找不到文件夹{res_path}")
    return df_data


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


def recursion_load_deg_enrichment_csv(gpf_path):
    """
    :param gpf_path: 需要读入的DEG enrichment结果路径，如：E:\\GPF
    :return: 返回拼接好的包含所有model结果的dataframe
    """
    df_data = pd.DataFrame()
    if os.path.isdir(gpf_path):
        for model in os.listdir(gpf_path):
            if os.path.isdir(os.path.join(gpf_path, model)):
                model_name = os.path.basename(model)
            else:
                continue
            for table_dir in os.listdir(os.path.join(gpf_path, model)):
                lfc = float(table_dir.strip().split('_')[0].replace('logFC', ''))
                padj = float(table_dir.strip().split('_')[1].replace('padj', ''))
                # print(model_name, lfc , padj)
                for compare in os.listdir(os.path.join(gpf_path, model, table_dir)):
                    comp1 = compare.strip().split('_')[0]
                    comp2 = compare.strip().split('_')[2]
                    # print(comp1, comp2)
                    for file in os.listdir(os.path.join(gpf_path, model, table_dir, compare)):
                        # 匹配含down和up的文件名，分别读入
                        if file.endswith('down.csv'):
                            tmp_df = helper.csv_to_data_frame(os.path.join(gpf_path, model, table_dir, compare, file),
                                                              {})
                            tmp_df['model_type'] = model_name
                            tmp_df['comp1'] = comp1
                            tmp_df['comp2'] = comp2
                            tmp_df['lfc_threshold'] = lfc
                            tmp_df['padj_threshold'] = padj
                            tmp_df['regulation'] = 'down'
                            if not tmp_df.empty:
                                tmp_df = check_is_represent_term(tmp_df,
                                                                 os.path.join(gpf_path, model, table_dir, compare,
                                                                              file))
                                df_data = pd.concat([df_data, tmp_df], ignore_index=True)
                        elif file.endswith('up.csv'):
                            tmp_df = helper.csv_to_data_frame(os.path.join(gpf_path, model, table_dir, compare, file),
                                                              {})
                            tmp_df['model_type'] = model_name
                            tmp_df['comp1'] = comp1
                            tmp_df['comp2'] = comp2
                            tmp_df['lfc_threshold'] = lfc
                            tmp_df['padj_threshold'] = padj
                            tmp_df['regulation'] = 'up'
                            if not tmp_df.empty:
                                tmp_df = check_is_represent_term(tmp_df,
                                                                 os.path.join(gpf_path, model, table_dir, compare,
                                                                              file))
                                df_data = pd.concat([df_data, tmp_df], ignore_index=True)
                    # print(df_data)
    return df_data


def recursion_load_gsea_enrichment_csv(gsea_path):
    """
    :param gsea_path: 需要读入的GSEA enrichment结果路径，如：E:\\GSEA
    :return: 返回拼接好的包含所有model结果的dataframe
    """
    df_data = pd.DataFrame()
    if os.path.isdir(gsea_path):
        for model in os.listdir(gsea_path):
            if os.path.isdir(os.path.join(gsea_path, model)):
                model_name = os.path.basename(model)
            else:
                continue
            for compare in os.listdir(os.path.join(gsea_path, model)):
                comp1 = compare.strip().split('_')[0]
                comp2 = compare.strip().split('_')[2]
                # print(comp1, comp2)
                for file in os.listdir(os.path.join(gsea_path, model, compare)):
                    # 匹配含csv的文件名读入
                    if file.endswith('.csv'):
                        tmp_df = helper.csv_to_data_frame(os.path.join(gsea_path, model, compare, file),
                                                          {'ID': 'msigdb_id'})
                        tmp_df['model_type'] = model_name
                        tmp_df['comp1'] = comp1
                        tmp_df['comp2'] = comp2
                        if not tmp_df.empty:
                            tmp_df = check_is_represent_term(tmp_df, os.path.join(gsea_path, model, compare, file),
                                                             method='gsea')
                            df_data = pd.concat([df_data, tmp_df], ignore_index=True)
    return df_data
