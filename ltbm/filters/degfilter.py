# filters.py
from ltbm.models import DegTable, DegEnrichmentTable
from django_filters import rest_framework as filters


class DegTableFilter(filters.FilterSet):

    def abs_gt(self, queryset, name, value):
        if value < 0:
            value = -value
        return queryset.filter(**{f'{name}__gt': value}).union(queryset.filter(**{f'{name}__lte': value * -1}))

    max_padj = filters.NumberFilter(field_name="padj", lookup_expr='lte', help_text="过滤FDR的阈值上限 建议0.01")
    min_lfc = filters.NumberFilter(field_name="log2FoldChange", method='abs_gt',
                                   help_text="过滤LFC的绝对值阈值下限 建议1")

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


class DegEnrichFilter(filters.FilterSet):
    class Meta:
        model = DegEnrichmentTable  # 模型名
        fields = {
            # 不必要的
            'source': ['exact'],
            # 必要的
            'model_type': ['exact'],
            'comp1': ['exact'],
            'comp2': ['exact'],
            'lfc_threshold': ['exact'],
            'padj_threshold': ['exact'],
            'regulation': ['exact'],
        }