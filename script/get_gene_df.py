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
