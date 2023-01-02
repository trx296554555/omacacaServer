from rest_framework import serializers
from ltbm.models import DegTable, DegEnrichmentTable, GseaEnrichmentTable


# ModelSerializer类能够让你自动创建一个具有模型中相应字段的Serializer类
class DegTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = DegTable
        # fields = "__all__"
        exclude = ['id', 'model_type', 'comp1', 'comp2']


class DegEnrichSerializers(serializers.ModelSerializer):
    class Meta:
        model = DegEnrichmentTable
        # fields = "__all__"
        exclude = ['id', 'model_type', 'comp1', 'comp2', 'lfc_threshold','padj_threshold']

class GseaEnrichSerializers(serializers.ModelSerializer):
    class Meta:
        model = GseaEnrichmentTable
        # fields = "__all__"
        exclude = ['id', 'model_type', 'comp1', 'comp2']