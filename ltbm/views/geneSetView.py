from ltbm.serializers import geneSetSer
from ltbm.models import VpaTable, GeneVstExpTable
from ltbm.filters import VpaTableFilter, GeneVstExpTableFilter

from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination


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
