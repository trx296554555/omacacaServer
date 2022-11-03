from rest_framework import serializers
from ..models import DegTable


# ModelSerializer类能够让你自动创建一个具有模型中相应字段的Serializer类
class DegTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = DegTable

        fields = "__all__"
        # exclude = ['id', 'pub_date']

# TODO 1.禁用put post delete 只用get get/1
# TODO 2.有一个filter的 查询方式 能够条件筛选
# TODO 3.分页查询 备选


test = DegTableSerializers()