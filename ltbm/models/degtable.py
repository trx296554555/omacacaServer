from django.db import models


class DegTable(models.Model):
    """
    DEG 差异表达结果
    """
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


class DegEnrichmentTable(models.Model):
    """
    DEG ORA 富集结果表
    """
    id = models.AutoField(primary_key=True)
    # csv表中原有的字段
    source = models.CharField(max_length=32, verbose_name="Source")
    term_name = models.TextField(verbose_name="Term Name", help_text='Enrichment Term Name')
    term_id = models.TextField(verbose_name="Term ID", help_text='Enrichment Term Uniq ID')
    adjusted_p_value = models.FloatField(verbose_name="Adjusted P-value")
    negative_log10_of_adjusted_p_value = models.FloatField(verbose_name="-log10(Adjusted P-value)")
    term_size = models.IntegerField(verbose_name="Term Size")
    query_size = models.IntegerField(verbose_name="Query Size")
    intersection_size = models.IntegerField(verbose_name="Intersection Size")
    effective_domain_size = models.IntegerField(verbose_name="Effective Domain Size")
    intersections = models.TextField(verbose_name="Intersections")
    # 根据csv表来源不同，添加的字段
    model_type = models.CharField(max_length=8, verbose_name="Model")
    comp1 = models.CharField(max_length=20, verbose_name="Group1")
    comp2 = models.CharField(max_length=20, verbose_name="Group2")
    lfc_threshold = models.FloatField(verbose_name="LFC_threshold")
    padj_threshold = models.FloatField(verbose_name="P_adj_threshold")
    regulation = models.CharField(max_length=8, verbose_name="Regulation")
    represent_term_wsc = models.BooleanField(verbose_name="Represent_term_wsc")
    represent_term_ap = models.BooleanField(verbose_name="Represent_term_ap")
    # 重新计算的字段
    rich_factor = models.FloatField(verbose_name="Rich Factor")

    class Meta:
        app_label = 'ltbm'


class GseaEnrichmentTable(models.Model):
    """
    DEG GSEA 富集结果表
    """
    id = models.AutoField(primary_key=True)
    # csv表中原有的字段
    source = models.CharField(max_length=32, verbose_name="Source")
    term_id = models.TextField(verbose_name="Term ID", help_text='Enrichment Term Uniq ID')
    term_name = models.TextField(verbose_name="Term Name", help_text='Enrichment Term Name')

    msigdb_id = models.TextField(verbose_name="MSigDB ID", help_text='MSigDB ID')
    setsize = models.IntegerField(db_column='setSize', verbose_name="Set Size")
    enrichmentscore = models.FloatField(db_column='enrichmentScore', verbose_name="Enrichment Score")
    nes = models.FloatField(db_column='NES', verbose_name="NES")
    pvalue = models.FloatField(verbose_name="P-value")
    p_adjust = models.FloatField(db_column='p.adjust', blank=True, null=True, verbose_name="P-adjust")
    qvalues = models.FloatField(verbose_name="Q-values")
    rank = models.IntegerField(verbose_name="Rank")
    leading_edge = models.TextField(verbose_name="Leading Edge")
    leading_edge_number = models.IntegerField(verbose_name="Leading Edge Number")
    core_enrichment = models.TextField(verbose_name="Core Enrichment")
    # 根据csv表来源不同，添加的字段
    model_type = models.CharField(max_length=8, verbose_name="Model")
    comp1 = models.CharField(max_length=20, verbose_name="Group1")
    comp2 = models.CharField(max_length=20, verbose_name="Group2")
    represent_term_wsc = models.BooleanField(verbose_name="Represent_term_wsc")
    represent_term_ap = models.BooleanField(verbose_name="Represent_term_ap")
    # 重新计算的字段
    rich_factor = models.FloatField(verbose_name="Rich Factor")

    class Meta:
        app_label = 'ltbm'