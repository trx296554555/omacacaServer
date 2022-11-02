from rest_framework import serializers
from ..models import DegTable


# 针对模型设计序列化器 原始方法自己设定
# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     pub_date = serializers.DateField(allow_null=False)
#
#     def create(self, validated_data):
#         # 数据校验通将数据插入到数据库中
#         new_book = Book.objects.create(**self.validated_data)
#         return new_book
#
#     def update(self, instance, validated_data):
#         # 更新逻辑   serializer.validated_data
#         Book.objects.filter(pk=instance.pk).update(**validated_data)
#         updated_book = Book.objects.get(pk=instance.pk)
#         return updated_book

# ModelSerializer类能够让你自动创建一个具有模型中相应字段的Serializer类
class BookSerializers(serializers.ModelSerializer):
    date = serializers.DateField(source='pub_date')

    class Meta:
        model = DegTable
        # fields = "__all__"
        exclude = ['id', 'pub_date']
