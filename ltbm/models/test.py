from django.db import models


# class Book(models.Model):
#     title = models.CharField(max_length=32, verbose_name="书籍名称")
#     price = models.IntegerField(verbose_name="价格")
#     pub_date = models.DateField(verbose_name="出版日期")
#
#     class Meta:
#         app_label = 'ltbm'


class DegTable(models.Model):
    uniq_num = models.IntegerField(verbose_name="uniq_num")
    gene_id = models.CharField(max_length=32, verbose_name="Ensemble ID")
    baseMean = models.FloatField(verbose_name="baseMean")
    log2FoldChange = models.FloatField(verbose_name="log2FoldChange")
    lfcSE = models.FloatField(verbose_name="lfcSE")
    stat = models.FloatField(verbose_name="stat")
    p_value = models.FloatField(verbose_name="P_value")
    p_adj = models.FloatField(verbose_name="P_adj")
    model_type = models.CharField(max_length=32, verbose_name="Model")
    comp1 = models.CharField(max_length=32, verbose_name="Group1")
    comp2 = models.CharField(max_length=32, verbose_name="Group2")

    class Meta:
        app_label = 'ltbm'
