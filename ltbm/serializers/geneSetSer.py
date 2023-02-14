from rest_framework import serializers
from ltbm.models import VpaTable, GeneVstExpTable, TsaTable, TsaEnrichmentTable
from ltbm.models import WgcnaModuleTraitTable, WgcnaGSMMtable, WgcnaEnrichmentTable, WgcnaTop30NetworkTable, \
    WgcnaModuleInfoTable


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


class TsaTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = TsaTable
        # fields = "__all__"
        exclude = ['id']


class TsaEnrichmentTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = TsaEnrichmentTable
        # fields = "__all__"
        exclude = ['id']


class WgcnaModuleTraitTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = WgcnaModuleTraitTable
        # fields = "__all__"
        exclude = ['id']


class WgcnaGSMMtableSerializer(serializers.ModelSerializer):
    class Meta:
        model = WgcnaGSMMtable
        # fields = "__all__"
        exclude = ['id']


class WgcnaEnrichmentTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = WgcnaEnrichmentTable
        # fields = "__all__"
        exclude = ['id']


class WgcnaTop30NetworkTableSerializers(serializers.ModelSerializer):
    class Meta:
        model = WgcnaTop30NetworkTable
        # fields = "__all__"
        exclude = ['id']


class WgcnaModuleInfoTableSerializers(serializers.ModelSerializer):
    gsmm_info = WgcnaGSMMtableSerializer(many=True)
    enrichment = WgcnaEnrichmentTableSerializers(many=True)
    network = WgcnaTop30NetworkTableSerializers(many=True)

    class Meta:
        model = WgcnaModuleInfoTable
        # fields = "__all__"
        fields = ['module', 'gene_num', 'label', 'gsmm_info', 'enrichment', 'network']
        # exclude = ['id']
