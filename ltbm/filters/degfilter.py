# filters.py
from ltbm.models import DegTable
from django_filters import rest_framework as filters


class DegTableFilter(filters.FilterSet):
    max_padj = filters.NumberFilter(field_name="padj", lookup_expr='lte', help_text="过滤FDR的阈值上限 建议0.01")

    # min_padj = filters.NumberFilter(field_name="padj", lookup_expr='gte')

    class Meta:
        model = DegTable  # 模型名
        fields = {
            'gene_id_ENSG': ['exact'],
            'log2FoldChange': ['gte', 'lte'],
            # 'padj': ['gte', 'lte'],
            # 'model_type': ['icontains'],
            'model_type': ['exact'],
            'comp1': ['exact'],
            'comp2': ['exact'],
        }
