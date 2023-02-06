from ltbm.models import VpaTable, GeneVstExpTable
from django_filters import rest_framework as filters


class VpaTableFilter(filters.FilterSet):
    class Meta:
        model = VpaTable  # 模型名
        fields = {
            'gene_id_ENSG': ['exact'],
        }


class GeneVstExpTableFilter(filters.FilterSet):
    class Meta:
        model = GeneVstExpTable  # 模型名
        fields = {
            'gene_id_ENSG': ['exact'],
            'model_type': ['exact']
        }
