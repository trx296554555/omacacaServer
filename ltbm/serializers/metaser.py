from rest_framework import serializers
from ltbm.models import Metatable


# ModelSerializer类能够让你自动创建一个具有模型中相应字段的Serializer类
class MetaMetaSerializers(serializers.ModelSerializer):
    """
    返回所有元信息
    """

    class Meta:
        model = Metatable
        # fields = ['sample_id', 'individual', 'genus', 'species', 'taxonomy_id', 'stage', 'age', 'sex', 'is_adult',
        #           'is_lactation', 'breast_milk', 'breeding_condition', 'envs', 'envs_info', 'diet', 'state',
        #           'state_info', 'sampling_date', 'sampling_timestamp']
        exclude = ['id']


class MetaUmapSerializers(serializers.ModelSerializer):
    """
    返回用于绘制Umap的元信息
    """

    class Meta:
        model = Metatable
        fields = ['lang', 'sample_id', 'individual', 'stage', 'age', 'sex', 'breeding_condition', 'envs', 'envs_info',
                  'diet',
                  'state', 'state_info', 'sampling_date',
                  'm1_umap_dimension_1', 'm1_umap_dimension_2', 'm4_umap_dimension_1', 'm4_umap_dimension_2']
        # exclude = ['id']
