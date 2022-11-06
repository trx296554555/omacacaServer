from rest_framework import serializers
from ltbm.models import DegTable


# ModelSerializer类能够让你自动创建一个具有模型中相应字段的Serializer类
class DegTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = DegTable
        # fields = "__all__"
        exclude = ['id', 'model_type', 'comp1', 'comp2']
