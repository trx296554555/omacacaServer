from django.db import models


class VpaTable(models.Model):
    """
    VPA 结果表
    """
    id = models.AutoField(primary_key=True)
    gene_id_ENSG = models.CharField(max_length=32, verbose_name="Ensemble ID", help_text='Ensemble Gene Uniq ID')
    # csv表中原有的字段
    individual = models.FloatField(verbose_name="Individual")
    age = models.FloatField(verbose_name="Age")
    condition = models.FloatField(verbose_name="Condition")
    rin = models.FloatField(verbose_name="RIN")
    hemoglobin = models.FloatField(verbose_name="Hemoglobin")
    sex = models.FloatField(verbose_name="Sex")
    state = models.FloatField(verbose_name="State")
    residuals = models.FloatField(verbose_name="Residuals")

    class Meta:
        app_label = 'ltbm'


class TsaTable(models.Model):
    """
    TSA 结果表
    """
    id = models.AutoField(primary_key=True)
    gene_id_ENSG = models.CharField(max_length=32, verbose_name="Ensemble ID", help_text='Ensemble Gene Uniq ID')
    # csv表中原有的字段
    cluster = models.CharField(max_length=16, verbose_name="Cluster")
    is_core = models.BooleanField(verbose_name="Is Core")
    membership = models.FloatField(verbose_name="Membership")

    class Meta:
        app_label = 'ltbm'


class TsaEnrichmentTable(models.Model):
    """
    TSA 富集结果表
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
    cluster = models.CharField(max_length=16, verbose_name="Cluster")
    represent_term_wsc = models.BooleanField(verbose_name="Represent_term_wsc")
    represent_term_ap = models.BooleanField(verbose_name="Represent_term_ap")
    # 重新计算的字段
    rich_factor = models.FloatField(verbose_name="Rich Factor")

    class Meta:
        app_label = 'ltbm'


class WgcnaModuleTraitTable(models.Model):
    """
    WGCNA 模块特征关系表
    """
    id = models.AutoField(primary_key=True)
    # csv表中原有的字段
    x = models.CharField(max_length=32, verbose_name="X")
    y = models.CharField(max_length=32, verbose_name="Y")
    correlation_value = models.FloatField(verbose_name="Up")
    p_value = models.FloatField(verbose_name="Down")
    # 根据csv表来源不同，添加的字段
    analyse = models.CharField(max_length=8, verbose_name="Analyse")
    model_type = models.CharField(max_length=8, verbose_name="Model")

    class Meta:
        app_label = 'ltbm'


class WgcnaModuleInfoTable(models.Model):
    """
    WGCNA 模块信息总表 用于实现一对多关系
    """
    # id = models.AutoField(primary_key=True)

    module = models.CharField(max_length=32, verbose_name="Module", primary_key=True)
    gene_num = models.IntegerField(verbose_name="Gene Num")
    color = models.CharField(max_length=32, verbose_name="Color")
    label = models.IntegerField(verbose_name="Label")
    analyse = models.CharField(max_length=8, verbose_name="Analyse")
    model_type = models.CharField(max_length=8, verbose_name="Model")

    class Meta:
        app_label = 'ltbm'


class WgcnaGSMMtable(models.Model):
    """
    WGCNA Gene-Trait Significance 和 Gene-Module Membership 结果表
    """
    id = models.AutoField(primary_key=True)
    # csv表中原有的字段
    gene_id_ENSG = models.CharField(max_length=32, verbose_name="Ensemble ID", help_text='Ensemble Gene Uniq ID')
    module = models.ForeignKey('WgcnaModuleInfoTable', on_delete=models.CASCADE, related_name='gsmm_info',
                               verbose_name="Module")
    gs_age = models.FloatField(db_column='GS.Age')
    p_gs_age = models.FloatField(db_column='p.GS.Age')
    gs_sex = models.FloatField(db_column='GS.Sex')
    p_gs_sex = models.FloatField(db_column='p.GS.Sex')
    gs_state = models.FloatField(db_column='GS.State')
    p_gs_state = models.FloatField(db_column='p.GS.State')
    gs_rin = models.FloatField(db_column='GS.RIN')
    p_gs_rin = models.FloatField(db_column='p.GS.RIN')
    gs_hemoglobin_raw = models.FloatField(db_column='GS.Hemoglobin_raw')
    p_gs_hemoglobin_raw = models.FloatField(db_column='p.GS.Hemoglobin_raw')
    gs_conditionc1 = models.FloatField(db_column='GS.ConditionC1')
    p_gs_conditionc1 = models.FloatField(db_column='p.GS.ConditionC1')
    gs_conditionc2 = models.FloatField(db_column='GS.ConditionC2')
    p_gs_conditionc2 = models.FloatField(db_column='p.GS.ConditionC2')
    gs_conditionc3 = models.FloatField(db_column='GS.ConditionC3')
    p_gs_conditionc3 = models.FloatField(db_column='p.GS.ConditionC3')
    gs_conditionc4 = models.FloatField(db_column='GS.ConditionC4')
    p_gs_conditionc4 = models.FloatField(db_column='p.GS.ConditionC4')
    gs_conditionc5 = models.FloatField(db_column='GS.ConditionC5')
    p_gs_conditionc5 = models.FloatField(db_column='p.GS.ConditionC5')
    mm_blue = models.FloatField(db_column='MM_blue')
    mm_magenta = models.FloatField(db_column='MM_magenta')
    mm_pink = models.FloatField(db_column='MM_pink')
    mm_brown = models.FloatField(db_column='MM_brown')
    mm_green = models.FloatField(db_column='MM_green')
    mm_greenyellow = models.FloatField(db_column='MM_greenyellow')
    mm_turquoise = models.FloatField(db_column='MM_turquoise')
    mm_lightcyan = models.FloatField(db_column='MM_lightcyan')
    mm_salmon = models.FloatField(db_column='MM_salmon')
    mm_yellow = models.FloatField(db_column='MM_yellow')
    mm_midnightblue = models.FloatField(db_column='MM_midnightblue')
    mm_grey60 = models.FloatField(db_column='MM_grey60')
    mm_black = models.FloatField(db_column='MM_black')
    mm_tan = models.FloatField(db_column='MM_tan')
    mm_purple = models.FloatField(db_column='MM_purple')
    mm_cyan = models.FloatField(db_column='MM_cyan')
    mm_red = models.FloatField(db_column='MM_red')
    mm_grey = models.FloatField(db_column='MM_grey')
    p_mm_blue = models.FloatField(db_column='p_MM_blue')
    p_mm_magenta = models.FloatField(db_column='p_MM_magenta')
    p_mm_pink = models.FloatField(db_column='p_MM_pink')
    p_mm_brown = models.FloatField(db_column='p_MM_brown')
    p_mm_green = models.FloatField(db_column='p_MM_green')
    p_mm_greenyellow = models.FloatField(db_column='p_MM_greenyellow')
    p_mm_turquoise = models.FloatField(db_column='p_MM_turquoise')
    p_mm_lightcyan = models.FloatField(db_column='p_MM_lightcyan')
    p_mm_salmon = models.FloatField(db_column='p_MM_salmon')
    p_mm_yellow = models.FloatField(db_column='p_MM_yellow')
    p_mm_midnightblue = models.FloatField(db_column='p_MM_midnightblue')
    p_mm_grey60 = models.FloatField(db_column='p_MM_grey60')
    p_mm_black = models.FloatField(db_column='p_MM_black')
    p_mm_tan = models.FloatField(db_column='p_MM_tan')
    p_mm_purple = models.FloatField(db_column='p_MM_purple')
    p_mm_cyan = models.FloatField(db_column='p_MM_cyan')
    p_mm_red = models.FloatField(db_column='p_MM_red')
    p_mm_grey = models.FloatField(db_column='p_MM_grey')
    analyse = models.CharField(max_length=8, verbose_name="Analyse")
    model_type = models.CharField(max_length=8, verbose_name="Model")

    class Meta:
        app_label = 'ltbm'


class WgcnaEnrichmentTable(models.Model):
    """
    WGCNA Enrichment Table
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
    module = models.ForeignKey('WgcnaModuleInfoTable', on_delete=models.CASCADE, related_name='enrichment',
                               verbose_name="Module")
    represent_term_wsc = models.BooleanField(verbose_name="Represent_term_wsc")
    represent_term_ap = models.BooleanField(verbose_name="Represent_term_ap")
    # 重新计算的字段
    rich_factor = models.FloatField(verbose_name="Rich Factor")


class WgcnaTop30NetworkTable(models.Model):
    """
    WGCNA Top30 Network Table
    """
    id = models.AutoField(primary_key=True)
    # csv表中原有的字段
    fromnode = models.CharField(max_length=32, db_column='fromNode', blank=True, null=True)
    tonode = models.CharField(max_length=32, db_column='toNode', blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    direction = models.TextField(blank=True, null=True)
    fromaltname = models.CharField(max_length=32, db_column='fromAltName', blank=True, null=True)
    toaltname = models.CharField(max_length=32, db_column='toAltName', blank=True, null=True)
    # 根据csv表来源不同，添加的字段
    model_type = models.CharField(max_length=8, verbose_name="Model")
    module = models.ForeignKey('WgcnaModuleInfoTable', on_delete=models.CASCADE, related_name='network',
                               verbose_name="Module")


class GeneVstExpTable(models.Model):
    id = models.AutoField(primary_key=True)
    gene_id_ENSG = models.CharField(max_length=32, verbose_name="Ensemble ID", help_text='Ensemble Gene Uniq ID')
    # csv表中原有的字段
    bcr01_a = models.FloatField(db_column='BCR01.A')
    bcr02_a = models.FloatField(db_column='BCR02.A')
    bcr03_a = models.FloatField(db_column='BCR03.A')
    bcr06_a = models.FloatField(db_column='BCR06.A')
    bcr07_a = models.FloatField(db_column='BCR07.A')
    bcr08_a = models.FloatField(db_column='BCR08.A')
    bcr09_a = models.FloatField(db_column='BCR09.A')
    bcr10_a = models.FloatField(db_column='BCR10.A')
    bcr11_a = models.FloatField(db_column='BCR11.A')
    bcr12_a = models.FloatField(db_column='BCR12.A')
    bcr13_a = models.FloatField(db_column='BCR13.A')
    bcr14_a = models.FloatField(db_column='BCR14.A')
    bcr15_a = models.FloatField(db_column='BCR15.A')
    bcr16_a = models.FloatField(db_column='BCR16.A')
    bcr17_a = models.FloatField(db_column='BCR17.A')
    bcr18_a = models.FloatField(db_column='BCR18.A')
    bcr19_a = models.FloatField(db_column='BCR19.A')
    bcr20_a = models.FloatField(db_column='BCR20.A')
    bcr21_a = models.FloatField(db_column='BCR21.A')
    bcr01_b = models.FloatField(db_column='BCR01.B')
    bcr02_b = models.FloatField(db_column='BCR02.B')
    bcr03_b = models.FloatField(db_column='BCR03.B')
    bcr04_b = models.FloatField(db_column='BCR04.B')
    bcr05_b = models.FloatField(db_column='BCR05.B')
    bcr06_b = models.FloatField(db_column='BCR06.B')
    bcr07_b = models.FloatField(db_column='BCR07.B')
    bcr08_b = models.FloatField(db_column='BCR08.B')
    bcr09_b = models.FloatField(db_column='BCR09.B')
    bcr10_b = models.FloatField(db_column='BCR10.B')
    bcr11_b = models.FloatField(db_column='BCR11.B')
    bcr12_b = models.FloatField(db_column='BCR12.B')
    bcr13_b = models.FloatField(db_column='BCR13.B')
    bcr14_b = models.FloatField(db_column='BCR14.B')
    bcr15_b = models.FloatField(db_column='BCR15.B')
    bcr16_b = models.FloatField(db_column='BCR16.B')
    bcr17_b = models.FloatField(db_column='BCR17.B')
    bcr18_b = models.FloatField(db_column='BCR18.B')
    bcr19_b = models.FloatField(db_column='BCR19.B')
    bcr20_b = models.FloatField(db_column='BCR20.B')
    bcr21_b = models.FloatField(db_column='BCR21.B')
    bcr01_c = models.FloatField(db_column='BCR01.C')
    bcr02_c = models.FloatField(db_column='BCR02.C')
    bcr03_c = models.FloatField(db_column='BCR03.C')
    bcr04_c = models.FloatField(db_column='BCR04.C')
    bcr05_c = models.FloatField(db_column='BCR05.C')
    bcr06_c = models.FloatField(db_column='BCR06.C')
    bcr07_c = models.FloatField(db_column='BCR07.C')
    bcr08_c = models.FloatField(db_column='BCR08.C')
    bcr09_c = models.FloatField(db_column='BCR09.C')
    bcr10_c = models.FloatField(db_column='BCR10.C')
    bcr11_c = models.FloatField(db_column='BCR11.C')
    bcr12_c = models.FloatField(db_column='BCR12.C')
    bcr13_c = models.FloatField(db_column='BCR13.C')
    bcr14_c = models.FloatField(db_column='BCR14.C')
    bcr15_c = models.FloatField(db_column='BCR15.C')
    bcr16_c = models.FloatField(db_column='BCR16.C')
    bcr17_c = models.FloatField(db_column='BCR17.C')
    bcr18_c = models.FloatField(db_column='BCR18.C')
    bcr19_c = models.FloatField(db_column='BCR19.C')
    bcr20_c = models.FloatField(db_column='BCR20.C')
    bcr21_c = models.FloatField(db_column='BCR21.C')
    bcr01_d = models.FloatField(db_column='BCR01.D')
    bcr02_d = models.FloatField(db_column='BCR02.D')
    bcr03_d = models.FloatField(db_column='BCR03.D')
    bcr04_d = models.FloatField(db_column='BCR04.D')
    bcr05_d = models.FloatField(db_column='BCR05.D')
    bcr06_d = models.FloatField(db_column='BCR06.D')
    bcr07_d = models.FloatField(db_column='BCR07.D')
    bcr08_d = models.FloatField(db_column='BCR08.D')
    bcr09_d = models.FloatField(db_column='BCR09.D')
    bcr10_d = models.FloatField(db_column='BCR10.D')
    bcr11_d = models.FloatField(db_column='BCR11.D')
    bcr12_d = models.FloatField(db_column='BCR12.D')
    bcr13_d = models.FloatField(db_column='BCR13.D')
    bcr14_d = models.FloatField(db_column='BCR14.D')
    bcr15_d = models.FloatField(db_column='BCR15.D')
    bcr16_d = models.FloatField(db_column='BCR16.D')
    bcr17_d = models.FloatField(db_column='BCR17.D')
    bcr18_d = models.FloatField(db_column='BCR18.D')
    bcr19_d = models.FloatField(db_column='BCR19.D')
    bcr20_d = models.FloatField(db_column='BCR20.D')
    bcr21_d = models.FloatField(db_column='BCR21.D')
    bcr01_e = models.FloatField(db_column='BCR01.E')
    bcr02_e = models.FloatField(db_column='BCR02.E')
    bcr03_e = models.FloatField(db_column='BCR03.E')
    bcr04_e = models.FloatField(db_column='BCR04.E')
    bcr05_e = models.FloatField(db_column='BCR05.E')
    bcr06_e = models.FloatField(db_column='BCR06.E')
    bcr07_e = models.FloatField(db_column='BCR07.E')
    bcr08_e = models.FloatField(db_column='BCR08.E')
    bcr09_e = models.FloatField(db_column='BCR09.E')
    bcr10_e = models.FloatField(db_column='BCR10.E')
    bcr11_e = models.FloatField(db_column='BCR11.E')
    bcr12_e = models.FloatField(db_column='BCR12.E')
    bcr13_e = models.FloatField(db_column='BCR13.E')
    bcr14_e = models.FloatField(db_column='BCR14.E')
    bcr15_e = models.FloatField(db_column='BCR15.E')
    bcr16_e = models.FloatField(db_column='BCR16.E')
    bcr17_e = models.FloatField(db_column='BCR17.E')
    bcr18_e = models.FloatField(db_column='BCR18.E')
    bcr19_e = models.FloatField(db_column='BCR19.E')
    bcr20_e = models.FloatField(db_column='BCR20.E')
    bcr21_e = models.FloatField(db_column='BCR21.E')
    bcr01_f = models.FloatField(db_column='BCR01.F')
    bcr02_f = models.FloatField(db_column='BCR02.F')
    bcr03_f = models.FloatField(db_column='BCR03.F')
    bcr04_f = models.FloatField(db_column='BCR04.F')
    bcr05_f = models.FloatField(db_column='BCR05.F')
    bcr06_f = models.FloatField(db_column='BCR06.F')
    bcr07_f = models.FloatField(db_column='BCR07.F')
    bcr08_f = models.FloatField(db_column='BCR08.F')
    bcr09_f = models.FloatField(db_column='BCR09.F')
    bcr10_f = models.FloatField(db_column='BCR10.F')
    bcr11_f = models.FloatField(db_column='BCR11.F')
    bcr12_f = models.FloatField(db_column='BCR12.F')
    bcr13_f = models.FloatField(db_column='BCR13.F')
    bcr14_f = models.FloatField(db_column='BCR14.F')
    bcr15_f = models.FloatField(db_column='BCR15.F')
    bcr16_f = models.FloatField(db_column='BCR16.F')
    bcr17_f = models.FloatField(db_column='BCR17.F')
    bcr18_f = models.FloatField(db_column='BCR18.F')
    bcr19_f = models.FloatField(db_column='BCR19.F')
    bcr20_f = models.FloatField(db_column='BCR20.F')
    bcr21_f = models.FloatField(db_column='BCR21.F')
    bcr01_g = models.FloatField(db_column='BCR01.G')
    bcr02_g = models.FloatField(db_column='BCR02.G')
    bcr04_g = models.FloatField(db_column='BCR04.G')
    bcr05_g = models.FloatField(db_column='BCR05.G')
    bcr06_g = models.FloatField(db_column='BCR06.G')
    bcr07_g = models.FloatField(db_column='BCR07.G')
    bcr08_g = models.FloatField(db_column='BCR08.G')
    bcr09_g = models.FloatField(db_column='BCR09.G')
    bcr10_g = models.FloatField(db_column='BCR10.G')
    bcr11_g = models.FloatField(db_column='BCR11.G')
    bcr12_g = models.FloatField(db_column='BCR12.G')
    bcr13_g = models.FloatField(db_column='BCR13.G')
    bcr14_g = models.FloatField(db_column='BCR14.G')
    bcr15_g = models.FloatField(db_column='BCR15.G')
    bcr16_g = models.FloatField(db_column='BCR16.G')
    bcr17_g = models.FloatField(db_column='BCR17.G')
    bcr18_g = models.FloatField(db_column='BCR18.G')
    bcr19_g = models.FloatField(db_column='BCR19.G')
    bcr21_g = models.FloatField(db_column='BCR21.G')
    model_type = models.CharField(max_length=8, verbose_name="Model")
    mcr01 = models.FloatField(db_column='MCR01', blank=True, null=True)
    mcr02 = models.FloatField(db_column='MCR02', blank=True, null=True)
    mcr03 = models.FloatField(db_column='MCR03', blank=True, null=True)
    mcr05 = models.FloatField(db_column='MCR05', blank=True, null=True)
    mcr06 = models.FloatField(db_column='MCR06', blank=True, null=True)
    mcr07 = models.FloatField(db_column='MCR07', blank=True, null=True)
    mcr08 = models.FloatField(db_column='MCR08', blank=True, null=True)
    mcr09 = models.FloatField(db_column='MCR09', blank=True, null=True)
    mcr10 = models.FloatField(db_column='MCR10', blank=True, null=True)
    mcr11 = models.FloatField(db_column='MCR11', blank=True, null=True)
    mcr12 = models.FloatField(db_column='MCR12', blank=True, null=True)
    mcr14 = models.FloatField(db_column='MCR14', blank=True, null=True)
    mcr15 = models.FloatField(db_column='MCR15', blank=True, null=True)
    mcr16 = models.FloatField(db_column='MCR16', blank=True, null=True)
    mcr17 = models.FloatField(db_column='MCR17', blank=True, null=True)
    mcr18 = models.FloatField(db_column='MCR18', blank=True, null=True)
    mcr19 = models.FloatField(db_column='MCR19', blank=True, null=True)
    mcr20 = models.FloatField(db_column='MCR20', blank=True, null=True)
    mcr21 = models.FloatField(db_column='MCR21', blank=True, null=True)
    ocr01 = models.FloatField(db_column='OCR01', blank=True, null=True)
    ocr02 = models.FloatField(db_column='OCR02', blank=True, null=True)
    ocr03 = models.FloatField(db_column='OCR03', blank=True, null=True)
    ocr04 = models.FloatField(db_column='OCR04', blank=True, null=True)
    ocr05 = models.FloatField(db_column='OCR05', blank=True, null=True)
    ocr06 = models.FloatField(db_column='OCR06', blank=True, null=True)
    ocr07 = models.FloatField(db_column='OCR07', blank=True, null=True)
    ocr08 = models.FloatField(db_column='OCR08', blank=True, null=True)
    ocr09 = models.FloatField(db_column='OCR09', blank=True, null=True)
    ocr10 = models.FloatField(db_column='OCR10', blank=True, null=True)
    ocr11 = models.FloatField(db_column='OCR11', blank=True, null=True)
    ocr12 = models.FloatField(db_column='OCR12', blank=True, null=True)
    ocr13 = models.FloatField(db_column='OCR13', blank=True, null=True)
    ocr14 = models.FloatField(db_column='OCR14', blank=True, null=True)
    ocr15 = models.FloatField(db_column='OCR15', blank=True, null=True)
    ocr16 = models.FloatField(db_column='OCR16', blank=True, null=True)
    ocr17 = models.FloatField(db_column='OCR17', blank=True, null=True)
    ocr18 = models.FloatField(db_column='OCR18', blank=True, null=True)
    ocr19 = models.FloatField(db_column='OCR19', blank=True, null=True)
    ocr20 = models.FloatField(db_column='OCR20', blank=True, null=True)
    ocr21 = models.FloatField(db_column='OCR21', blank=True, null=True)
    ocr22 = models.FloatField(db_column='OCR22', blank=True, null=True)
