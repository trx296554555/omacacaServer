from ltbm.serializers import geneSetSer
from ltbm.models import Metatable
from ltbm.models import VpaTable, GeneVstExpTable, TsaTable, TsaEnrichmentTable
from ltbm.models import WgcnaModuleTraitTable, WgcnaModuleInfoTable, WgcnaGSMMtable
from ltbm.filters import VpaTableFilter, GeneVstExpTableFilter, WgcnaModuleInfoTableFilter

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

import pandas as pd


class GeneTablePagination(PageNumberPagination):
    # page_size = 20
    page_size_query_param = 'size'
    max_page_size = 20000
    ordering = ['id']


class VpaTableView(ListAPIView):
    """
    获取VpaTable表的数据
    """
    queryset = VpaTable.objects.all()
    serializer_class = geneSetSer.VpaTableSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = VpaTableFilter  # 过滤类
    ordering_fields = ['Individual', 'Age', 'Condition', 'RIN', 'Hemoglobin', 'Sex', 'State', 'Residuals']  # 排序
    search_fields = ['gene_id_ENSG']
    pagination_class = GeneTablePagination  # 分页


class GeneVstExpTableView(ListAPIView):
    """
    获取标准化后的gene表达数据
    """
    queryset = GeneVstExpTable.objects.all()
    serializer_class = geneSetSer.GeneVstExpTableSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = GeneVstExpTableFilter  # 过滤类
    ordering_fields = ['gene_id_ENSG']  # 排序
    search_fields = ['gene_id_ENSG']
    pagination_class = GeneTablePagination  # 分页


class GeneVstExpGroupByView(ListAPIView):
    """
    获取标准化后的gene表达数据按指定的group分组 Parameters: model_type, gene_id_ENSG, groupby, lang
    """

    def list(self, request, *args, **kwargs):
        """
        Parameters: model_type, gene_id_ENSG, groupby, lang
        """
        model_type = self.request.query_params.get('model_type', 'M1Ta')
        gene_id_ENSG = self.request.query_params.get('gene_id_ENSG', None)
        group_by = self.request.query_params.get('groupby', 'stage')
        lang = self.request.query_params.get('lang', 'zh_CN')
        if model_type == 'M1Ta' and lang == 'en':
            meta_data = Metatable.objects.filter(lang=lang, is_adult='F')
        elif model_type == 'M1Ta' and lang == 'zh_CN':
            meta_data = Metatable.objects.filter(lang=lang, is_adult='否')
        elif model_type == 'M4Ta':
            meta_data = Metatable.objects.filter(lang=lang)
        exp_data = GeneVstExpTable.objects.filter(gene_id_ENSG=gene_id_ENSG, model_type=model_type)
        # 转为dataframe
        meta_data = pd.DataFrame(list(meta_data.values()))
        # 取sample 和 group 列
        meta_data = meta_data[['sample_id', group_by]]
        exp_data = pd.DataFrame(list(exp_data.values()))
        # 转置
        exp_data = exp_data.T
        # 将行索引转化为列
        exp_data.reset_index(inplace=True)
        # 并修改列名为sample_id和exp
        exp_data.columns = ['sample_id', 'exp']
        # 将sample_id列中的值转化为大写字符
        exp_data['sample_id'] = exp_data['sample_id'].str.upper()
        # 将sample_id列中的值替换_ 为 .
        exp_data['sample_id'] = exp_data['sample_id'].str.replace('_', '.')
        # 合并两个dataframe
        out_data = pd.merge(meta_data, exp_data, on='sample_id')
        # 将exp列转化为float类型
        out_data['exp'] = out_data['exp'].astype(float)
        # out_data中的nan值替换为0
        out_data = out_data.fillna(0)
        out_dict = out_data.to_dict(orient='records')
        # 获取out_data的分组数据并统计
        group_exp_df = out_data.groupby([group_by]).describe()
        group_exp_df = group_exp_df.fillna(0)
        describe_dict = group_exp_df['exp'].to_dict(orient="index")

        return Response({'data': out_dict, 'describe': describe_dict})


class TsaResView(ListAPIView):
    """
    获取TSA结果，重新，包括TSA的结果，以及TSA的富集结果 Parameters: cluster
    """

    def list(self, request, *args, **kwargs):
        """
        Parameters: cluster
        """
        cluster = self.request.query_params.get('cluster', None)

        model_tsa = TsaTable.objects.filter(cluster=cluster)
        model_tsa_enrichment = TsaEnrichmentTable.objects.filter(cluster=cluster)
        serializer_tsa = geneSetSer.TsaTableSerializers(model_tsa, many=True)
        serializer_tsa_enrichment = geneSetSer.TsaEnrichmentTableSerializers(model_tsa_enrichment, many=True)
        return Response({'tsa': serializer_tsa.data, 'tsa_enrichment': serializer_tsa_enrichment.data})


class WgcnaMtTableView(ListAPIView):
    """
    获取WGCNA的 Module−trait relationships 结果
    """
    queryset = WgcnaModuleTraitTable.objects.all()
    serializer_class = geneSetSer.WgcnaModuleTraitTableSerializers
    pagination_class = GeneTablePagination  # 分页


class WgcnaResView(ListAPIView):
    """
    获取WGCNA的 Gene Set Module Membership 结果
    """
    queryset = WgcnaModuleInfoTable.objects.all()
    serializer_class = geneSetSer.WgcnaModuleInfoTableSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = WgcnaModuleInfoTableFilter  # 过滤类
    ordering_fields = ['module', 'gene_num']  # 排序
