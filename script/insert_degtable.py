import pandas as pd
import helper
import os


def load_csv_from_local(res_path):
    """
    :param res_path: 需要读入的RES结果路径，如：E:\RES
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
                    csv_file = os.path.join(res_path, model, root_value, table_dir, model_name + '_' + table_dir + '.csv')
                    tmp_df = helper.csv_to_data_frame(csv_file, {'Unnamed: 0': 'gene_id'})
                    tmp_df['model_type'] = model
                    tmp_df['comp1'] = comp1_name
                    tmp_df['comp2'] = comp2_name
                    df_data = pd.concat([df_data, tmp_df], ignore_index=True)
    return df_data


# load_csv_from_local(r'E:\RES')
