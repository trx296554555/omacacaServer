from django.db import models


class Metatable(models.Model):
    id = models.AutoField(primary_key=True)
    lang = models.TextField(db_column='Lang', blank=True, null=True)
    sample_id = models.TextField(db_column='Sample_ID', blank=True, null=True)
    individual = models.TextField(db_column='Individual', blank=True, null=True)
    genus = models.TextField(db_column='Genus', blank=True, null=True)
    species = models.TextField(db_column='Species', blank=True, null=True)
    taxonomy_id = models.IntegerField(db_column='Taxonomy_ID', blank=True, null=True)
    stage = models.TextField(db_column='Stage', blank=True, null=True)
    age = models.TextField(db_column='Age', blank=True, null=True)
    sex = models.TextField(db_column='Sex', blank=True, null=True)
    is_adult = models.TextField(db_column='Is_adult', blank=True, null=True)
    is_lactation = models.TextField(db_column='Is_lactation', blank=True, null=True)
    breast_milk = models.TextField(db_column='Breast_Milk', blank=True, null=True)
    breeding_condition = models.TextField(db_column='Breeding_Condition', blank=True, null=True)
    envs = models.TextField(db_column='Envs', blank=True, null=True)
    envs_info = models.TextField(db_column='Envs_Info', blank=True, null=True)
    diet = models.TextField(db_column='Diet', blank=True, null=True)
    state = models.TextField(db_column='State', blank=True, null=True)
    state_info = models.TextField(db_column='State_Info', blank=True, null=True)
    sampling_date = models.DateField(db_column='Sampling_Date', blank=True, null=True)
    sampling_timestamp = models.TextField(db_column='Sampling_Timestamp', blank=True, null=True)
    sample_type_transcriptome = models.TextField(db_column='Sample_Type_Transcriptome', blank=True, null=True)
    sequencing_type_transcriptome = models.TextField(db_column='Sequencing_Type_Transcriptome', blank=True, null=True)
    total_rna = models.FloatField(db_column='Total_RNA', blank=True, null=True)
    rin = models.FloatField(db_column='RIN', blank=True, null=True)
    hemoglobin = models.FloatField(db_column='Hemoglobin', blank=True, null=True)
    sequencing_platform_transcriptome = models.TextField(db_column='Sequencing_Platform_Transcriptome', blank=True,
                                                         null=True)
    instrument_model_transcriptome = models.TextField(db_column='Instrument_Model_Transcriptome', blank=True, null=True)
    library_transcriptome = models.TextField(db_column='Library_Transcriptome', blank=True, null=True)
    clean_reads_transcriptome = models.FloatField(db_column='Clean_Reads_Transcriptome', blank=True, null=True)
    clean_base_transcriptome = models.FloatField(db_column='Clean_Base_Transcriptome', blank=True, null=True)
    q20_transcriptome = models.FloatField(db_column='Q20_Transcriptome', blank=True, null=True)
    gc_content_transcriptome = models.FloatField(db_column='GC_Content_Transcriptome', blank=True, null=True)
    mapping_rate = models.FloatField(db_column='Mapping_Rate', blank=True, null=True)
    m1_umap_dimension_1 = models.FloatField(db_column='M1_UMAP_dimension_1', blank=True, null=True)
    m1_umap_dimension_2 = models.FloatField(db_column='M1_UMAP_dimension_2', blank=True, null=True)
    m4_umap_dimension_1 = models.FloatField(db_column='M4_UMAP_dimension_1', blank=True, null=True)
    m4_umap_dimension_2 = models.FloatField(db_column='M4_UMAP_dimension_2', blank=True, null=True)
    used_in_transcriptome_analysis = models.TextField(db_column='Used_in_transcriptome_analysis', blank=True, null=True)
    sample_type_metagenome = models.FloatField(db_column='Sample_Type_Metagenome', blank=True, null=True)
    sequencing_type_metagenome = models.FloatField(db_column='Sequencing_Type_Metagenome', blank=True, null=True)
    sequencing_platform_metagenome = models.FloatField(db_column='Sequencing_Platform_Metagenome', blank=True,
                                                       null=True)
    instrument_model_metagenome = models.FloatField(db_column='Instrument_Model_Metagenome', blank=True, null=True)
    library_metagenome = models.FloatField(db_column='Library_Metagenome', blank=True, null=True)
    clean_reads_metagenome = models.FloatField(db_column='Clean_Reads_Metagenome', blank=True, null=True)
    clean_base_metagenome = models.FloatField(db_column='Clean_Base_Metagenome', blank=True, null=True)
    q20_metagenome = models.FloatField(db_column='Q20_Metagenome', blank=True, null=True)
    gc_content_metagenome = models.FloatField(db_column='GC_Content_Metagenome', blank=True, null=True)
    non_hosts_reads = models.FloatField(db_column='Non_hosts_Reads', blank=True, null=True)
    classified_reads = models.FloatField(db_column='Classified_Reads', blank=True, null=True)
    absolute_classified_reads = models.FloatField(db_column='Absolute_Classified_Reads', blank=True, null=True)
    contig_num_seqs = models.FloatField(blank=True, null=True)
    contig_sum_len = models.FloatField(blank=True, null=True)
    contig_min_len = models.FloatField(blank=True, null=True)
    contig_avg_len = models.FloatField(blank=True, null=True)
    contig_max_len = models.FloatField(blank=True, null=True)
    used_in_metagenome_analysis = models.TextField(db_column='Used_in_metagenome_analysis', blank=True, null=True)

    class Meta:
        app_label = 'ltbm'
