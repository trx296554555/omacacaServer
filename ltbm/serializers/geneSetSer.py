from rest_framework import serializers
from ltbm.models import VpaTable, GeneVstExpTable


class VpaTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = VpaTable
        # fields = "__all__"
        exclude = ['id']


class GeneVstExpTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = GeneVstExpTable
        # fields = "__all__"
        exclude = ['id', 'model_type']
