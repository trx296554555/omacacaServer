from rest_framework import serializers
from ltbm.models import DegTable, DegEnrichmentTable, GseaEnrichmentTable, DegHtmTable, DegStkTable


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
        exclude = ['id', 'model_type', 'comp1', 'comp2', 'lfc_threshold', 'padj_threshold']


class GseaEnrichSerializers(serializers.ModelSerializer):
    class Meta:
        model = GseaEnrichmentTable
        # fields = "__all__"
        exclude = ['id', 'model_type', 'comp1', 'comp2']


class DegHtmSerializers(serializers.ModelSerializer):
    class Meta:
        model = DegHtmTable
        # fields = "__all__"
        exclude = ['id', 'analyse', 'model_type', 'lfc_threshold', 'padj_threshold']


class DegStkSerializers(serializers.ModelSerializer):
    class Meta:
        model = DegStkTable
        # fields = "__all__"
        exclude = ['id', 'analyse', 'model_type', 'lfc_threshold', 'padj_threshold']
