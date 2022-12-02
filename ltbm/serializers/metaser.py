from rest_framework import serializers
from ltbm.models import Metatable


# ModelSerializer类能够让你自动创建一个具有模型中相应字段的Serializer类
class MetaMetaSerializers(serializers.ModelSerializer):
    """
    只返回元信息
    """

    class Meta:
        model = Metatable
        fields = ['sample_id', 'individual', 'genus', 'species', 'taxonomy_id', 'stage', 'age', 'sex', 'is_adult',
                  'is_lactation', 'breast_milk', 'breeding_condition', 'envs', 'envs_info', 'diet', 'state',
                  'state_info', 'sampling_date', 'sampling_timestamp']
        # exclude = ['id', 'model_type', 'comp1', 'comp2']
