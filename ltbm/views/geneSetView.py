from ltbm.serializers import geneSetSer
from ltbm.models import VpaTable, GeneVstExpTable, TsaTable, TsaEnrichmentTable
from ltbm.models import WgcnaModuleTraitTable, WgcnaModuleInfoTable, WgcnaGSMMtable
from ltbm.filters import VpaTableFilter, GeneVstExpTableFilter, WgcnaModuleInfoTableFilter

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


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


class TsaResView(ListAPIView):
    def list(self, request, *args, **kwargs):
        """
        获取TSA结果，重新，包括TSA的结果，以及TSA的富集结果
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
