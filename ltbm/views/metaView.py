from ltbm.serializers import metaSer
from ltbm.models import Metatable
from ltbm.filters import MetaTableFilter
# 和 终极封装 ViewModelSet
# from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination


class MetaTablePagination(PageNumberPagination):
    page_size_query_param = 'size'
    max_page_size = 400
    ordering = ['id']


class MetaTableView(ListAPIView):
    """
    获取样本信息的结果 meta info
    """
    queryset = Metatable.objects.all()
    serializer_class = metaSer.MetaMetaSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = MetaTableFilter  # 过滤类
    ordering_fields = ['stage', 'sex', 'individual', 'breeding_condition']  # 排序
    search_fields = ['sample_id']
    pagination_class = MetaTablePagination  # 分页


class UmapTableView(ListAPIView):
    """
    获取绘制 Umap Plot 的样本信息的结果
    """
    queryset = Metatable.objects.all()
    serializer_class = metaSer.MetaUmapSerializers
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_class = MetaTableFilter  # 过滤类
    ordering_fields = ['stage', 'sex', 'individual', 'breeding_condition']  # 排序
    search_fields = ['sample_id']
    pagination_class = MetaTablePagination  # 分页
