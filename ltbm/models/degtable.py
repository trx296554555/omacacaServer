from django.db import models


class DegTable(models.Model):
    id = models.AutoField(primary_key=True)
    gene_id_ENSG = models.CharField(max_length=32, verbose_name="Ensemble ID", help_text='Ensemble Gene Uniq ID')
    baseMean = models.FloatField(verbose_name="baseMean")
    log2FoldChange = models.FloatField(verbose_name="log2FoldChange")
    lfcSE = models.FloatField(verbose_name="lfcSE")
    stat = models.FloatField(verbose_name="stat")
    pvalue = models.FloatField(verbose_name="P_value")
    padj = models.FloatField(verbose_name="P_adj")
    model_type = models.CharField(max_length=8, verbose_name="Model")
    comp1 = models.CharField(max_length=8, verbose_name="Group1")
    comp2 = models.CharField(max_length=8, verbose_name="Group2")

    class Meta:
        app_label = 'ltbm'
