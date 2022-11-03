# filters.py
from django_filters import rest_framework as filters
from ..models import DegTable


class DegTableFilter(filters.FilterSet):
    min_padj = filters.NumberFilter(field_name="padj", lookup_expr='gte')
    max_padj = filters.NumberFilter(field_name="padj", lookup_expr='lte')

    class Meta:
        model = DegTable  # 模型名
        fields = {
            'gene_id': ['icontains'],
            'log2FoldChange': ['gte', 'lte'],
            'padj': ['gte', 'lte'],
            'model_type': ['icontains'],
            'comp1': ['icontains'],
            'comp2': ['icontains'],
        }
