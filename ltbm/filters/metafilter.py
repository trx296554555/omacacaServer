from ltbm.models import Metatable
from django_filters import rest_framework as filters


class MetaTableFilter(filters.FilterSet):
    class Meta:
        model = Metatable  # 模型名
        fields = {
            'lang': ['exact'],
            'sample_id': ['exact'],
        }
