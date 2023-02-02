import json
import os
import re

import pandas as pd


def statistical_num(info, up_list, down_list):
    if len(up_list) != len(down_list):
        print("error")
        exit()
    stat_list = []
    model_type = info.group(1)
    lfc_threshold = info.group(2)
    padj_threshold = info.group(3)
    for index in range(len(up_list)):
        out_dict = {}
        filename = up_list[index]
        title = re.match('.*geneID_(.*)_VS_(.*)_up.txt', filename)
        out_dict["X"] = title.group(1)
        out_dict["Y"] = title.group(2)
        with open(filename) as ipt:
            out_dict["up"] = (len(ipt.readlines()))
        with open(filename.replace('up', 'down')) as ipt:
            out_dict["down"] = (len(ipt.readlines()))
        out_dict["size"] = out_dict["up"] + out_dict["down"]
        out_dict["rate"] = out_dict["up"] / out_dict["size"]
        out_dict["analyse"] = 'ora'
        out_dict["model_type"] = model_type
        out_dict["lfc_threshold"] = lfc_threshold
        out_dict["padj_threshold"] = padj_threshold
        stat_list.append(out_dict)

    return stat_list


def statistical_stk(info, file_list):
    stk_list = []
    model_type = info.group(1)
    lfc_threshold = info.group(2)
    padj_threshold = info.group(3)
    for file in file_list:
        title = re.match(r'(.*)\\(.*)\\M.*', file)
        ipt_data = pd.read_csv(file, index_col=0, encoding='gbk')
        if lfc_threshold == '2':
            lfc_bins = [-999, -4, -3.5, -3, -2.5, -2, 2, 2.5, 3, 3.5, 4, 999]
            lfc_label = ['-inf~-4', '-4~-3.5', '-3.5~-3', '-3~-2.5', '-2.5~-2', '0', '2~2.5', '2.5~3', '3~3.5', '3.5~4',
                         '4~inf']
        else:
            lfc_bins = [-999, -4, -3.5, -3, -2.5, -2, -1.5, -1, 1, 1.5, 2, 2.5, 3, 3.5, 4, 999]
            lfc_label = ['-inf~-4', '-4~-3.5', '-3.5~-3', '-3~-2.5', '-2.5~-2', '-2~-1.5', '-1.5~-1', '0', '1~1.5',
                         '1.5~2', '2~2.5', '2.5~3', '3~3.5', '3.5~4', '4~inf']

        ipt_data["lfc_label"] = pd.cut(x=ipt_data['log2FoldChange'], bins=lfc_bins, labels=lfc_label)
        series = ipt_data["lfc_label"].value_counts(sort=False)
        reverse_series = series.reindex(series.index[::-1])

        for i, j in zip(reverse_series.index, reverse_series):
            out_dict = {}
            out_dict.update({
                "category": title.group(2),
                "LogFC": i,
                "value": j,
                "analyse": 'ora',
                "model_type": model_type,
                "lfc_threshold": lfc_threshold,
                "padj_threshold": padj_threshold,
            })
            stk_list.append(out_dict)
    return stk_list


def forOraRes():
    work_path = r'D:\lab\猕猴\分析\转录组DEG\RES'
    htm_out_path = r'D:\lab\猕猴\可视化\Statistical\Htm\ORA'
    stk_out_path = r'D:\lab\猕猴\可视化\Statistical\Stk\ORA'

    all_dir_list = []
    all_htm_res_list = []
    all_stk_res_list = []
    for m_dir in os.listdir(work_path):
        pj_dirs = os.path.join(work_path, m_dir)
        for pj_dir in os.listdir(pj_dirs):
            out_dir = os.path.join(pj_dirs, pj_dir)
            if os.path.isdir(out_dir):
                all_dir_list.append(out_dir)

    for work_dir in all_dir_list:
        info = re.match(r'.*\\RES\\(.*)\\logFC(.)_padj(.+)', work_dir)
        up_file_list = []
        down_file_list = []
        otr_file_list = []
        for root, dirs, files in os.walk(work_dir):
            for file in files:
                up_file = re.match(r'.*\\geneID_(.*)_up.txt', os.path.join(root, file))
                down_file = re.match(r'.*\\geneID_(.*)_down.txt', os.path.join(root, file))
                otr_file = re.match(r'.*\\.*_(.*)_VS_OTHERS.csv', os.path.join(root, file))
                if up_file:
                    up_file_list.append(up_file.group(0))
                if down_file:
                    down_file_list.append(down_file.group(0))
                if otr_file:
                    otr_file_list.append(otr_file.group(0))

        # htm 结果输出
        htm_res = statistical_num(info, up_file_list, down_file_list)
        all_htm_res_list += htm_res

        # stk 结果输出
        stk_res = statistical_stk(info, otr_file_list)
        all_stk_res_list += stk_res

    df_htm_data = pd.DataFrame(all_htm_res_list)
    htm_file_name = os.path.join(htm_out_path, 'deg_num_statistical.csv')
    df_htm_data.to_csv(htm_file_name, index=False, encoding='utf-8')

    df_stk_data = pd.DataFrame(all_stk_res_list)
    stk_file_name = os.path.join(stk_out_path, 'deg_others_statistical.csv')
    df_stk_data.to_csv(stk_file_name, index=False, encoding='utf-8')

    return df_htm_data, df_stk_data


def statistical_gsea_num(res_list):
    if not isinstance(res_list, list):
        print("type error")
        exit()

    stat_list = []
    for gsea_res_file in res_list:
        info = re.match(r'.*\\(.*)_GSEA_(.*)_VS_(.*).csv', gsea_res_file)
        model_type = info.group(1)
        comp1 = info.group(2)
        comp2 = info.group(3)

        out_dict = {"X": comp1, "Y": comp2}

        ipt_data = pd.read_csv(gsea_res_file, index_col=0, encoding='gbk')
        up_num = len(ipt_data[ipt_data["NES"] >= 0])
        down_num = len(ipt_data[ipt_data["NES"] < 0])
        out_dict["up"] = up_num
        out_dict["down"] = down_num
        out_dict["size"] = out_dict["up"] + out_dict["down"]
        out_dict["rate"] = out_dict["up"] / out_dict["size"]
        out_dict["analyse"] = 'gsea'
        out_dict["model_type"] = model_type
        out_dict["lfc_threshold"] = 1
        out_dict["padj_threshold"] = 0.01
        stat_list.append(out_dict)

    return stat_list


def statistical_gsea_stk(res_list):
    stk_list = []
    for file in res_list:
        title = re.match(r'(.*)\\(.*)_GSEA_(.*).csv', file)
        ipt_data = pd.read_csv(file, index_col=0, encoding='gbk')
        nes_bins = [-3, -2.5, -2, -1.75, -1.5, -1, 1, 1.5, 1.75, 2, 2.5, 3]
        nes_label = ['-3~-2.5', '-2.5~-2', '-2~-1.75', '-1.75~-1.5', '-1.5~-1', '0', '1~1.5', '1.5~1.75', '1.75~2',
                     '2~2.5', '2.5~3']

        ipt_data["nes_label"] = pd.cut(x=ipt_data['NES'], bins=nes_bins, labels=nes_label)
        series = ipt_data["nes_label"].value_counts(sort=False)
        reverse_series = series.reindex(series.index[::-1])

        for i, j in zip(reverse_series.index, reverse_series):
            out_dict = {}
            out_dict.update({
                "category": title.group(3),
                "LogFC": i,
                "value": j,
                "analyse": 'gsea',
                "model_type": title.group(2),
                "lfc_threshold": 1,
                "padj_threshold": 0.01

            })
            stk_list.append(out_dict)
    return stk_list


def forGseaRes():
    work_path = r'D:\Lab\猕猴\分析\转录组DEG\GSEA'
    htm_out_path = r'D:\lab\猕猴\可视化\Statistical\Htm\GSEA'
    stk_out_path = r'D:\lab\猕猴\可视化\Statistical\Stk\GSEA'

    res_file_list = []
    otr_file_list = []
    # 遍历work_path下所有文件

    for root, dirs, files in os.walk(work_path):
        for file in files:
            res_file = re.match(r'(.*)\\(.*)_GSEA_(.*)_VS_(.*).csv', os.path.join(root, file))
            otr_file = re.match(r'(.*)\\(.*)_GSEA_(.*)_VS_OTHERS.csv', os.path.join(root, file))
            if res_file:
                res_file_list.append(res_file.group(0))
            if otr_file:
                otr_file_list.append(otr_file.group(0))

    all_htm_res_list = statistical_gsea_num(res_file_list)
    all_stk_res_list = statistical_gsea_stk(otr_file_list)

    df_htm_data = pd.DataFrame(all_htm_res_list)
    htm_file_name = os.path.join(htm_out_path, 'deg_num_statistical.csv')
    df_htm_data.to_csv(htm_file_name, index=False, encoding='utf-8')

    df_stk_data = pd.DataFrame(all_stk_res_list)
    stk_file_name = os.path.join(stk_out_path, 'deg_others_statistical.csv')
    df_stk_data.to_csv(stk_file_name, index=False, encoding='utf-8')
    return df_htm_data, df_stk_data


def get_htm_df():
    ora_htm_data, ora_stk_data = forOraRes()
    gsea_htm_data, gsea_stk_data = forGseaRes()
    all_htm_data = pd.concat([ora_htm_data, gsea_htm_data], axis=0)
    return all_htm_data


def get_stk_df():
    ora_htm_data, ora_stk_data = forOraRes()
    gsea_htm_data, gsea_stk_data = forGseaRes()
    all_stk_data = pd.concat([ora_stk_data, gsea_stk_data], axis=0)
    return all_stk_data
