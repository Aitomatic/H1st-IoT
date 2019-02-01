from django.contrib.admin import ModelAdmin, site, StackedInline
from django.db.models import Prefetch

from silk.profiling.profiler import silk_profile

from .forms import \
    EquipmentUniqueTypeGroupServiceConfigForm, \
    EquipmentUniqueTypeGroupMonitoredDataFieldConfigForm, \
    EquipmentProblemDiagnosisForm, \
    AlertForm

from .models import \
    GlobalConfig, \
    EquipmentUniqueTypeGroupDataFieldProfile, \
    EquipmentUniqueTypeGroupDataFieldPairwiseCorrelation, \
    EquipmentUniqueTypeGroupMonitoredDataFieldConfig, \
    EquipmentUniqueTypeGroupServiceConfig, \
    Blueprint, \
    EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfile, \
    EquipmentInstanceDailyRiskScore, \
    EquipmentProblemType, \
    EquipmentProblemDiagnosis, \
    Alert, \
    AlertDiagnosisStatus

from ..base.models import EquipmentDataField


class GlobalConfigAdmin(ModelAdmin):
    list_display = \
        'key', \
        'value', \
        'last_updated'

    show_full_result_count = False

    @silk_profile(name='ADMIN: Global Configs')
    def changelist_view(self, request, extra_context=None):
        return super(GlobalConfigAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='ADMIN: Global Config')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(GlobalConfigAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    GlobalConfig,
    admin_class=GlobalConfigAdmin)


class EquipmentUniqueTypeGroupDataFieldProfileAdmin(ModelAdmin):
    list_display = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        'to_date', \
        'valid_proportion', \
        'n_distinct_values', \
        'distinct_values', \
        'sample_min', \
        'outlier_rst_min', \
        'sample_quartile', \
        'sample_median', \
        'sample_3rd_quartile', \
        'outlier_rst_max', \
        'sample_max', \
        'last_updated'

    ordering = \
        'equipment_unique_type_group', \
        '-to_date', \
        '-n_distinct_values'

    list_filter = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'to_date', \
        'equipment_data_field__name'

    list_select_related = \
        'equipment_unique_type_group', 'equipment_unique_type_group__equipment_general_type', \
        'equipment_data_field', 'equipment_data_field__equipment_general_type', 'equipment_data_field__equipment_data_field_type', \
                                'equipment_data_field__data_type', 'equipment_data_field__numeric_measurement_unit'

    show_full_result_count = False

    search_fields = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'equipment_data_field__name'

    readonly_fields = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        'to_date', \
        'valid_proportion', \
        'distinct_values', \
        'n_distinct_values', \
        'sample_min', \
        'outlier_rst_min', \
        'sample_quartile', \
        'sample_median', \
        'sample_3rd_quartile', \
        'outlier_rst_max', \
        'sample_max', \
        'last_updated'

    @silk_profile(name='Admin: Equipment Unique Type Group Data Field Profiles')
    def changelist_view(self, request, extra_context=None):
        return super(EquipmentUniqueTypeGroupDataFieldProfileAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Equipment Unique Type Group Data Field Profile')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(EquipmentUniqueTypeGroupDataFieldProfileAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    EquipmentUniqueTypeGroupDataFieldProfile,
    admin_class=EquipmentUniqueTypeGroupDataFieldProfileAdmin)


class EquipmentUniqueTypeGroupDataFieldPairwiseCorrelationAdmin(ModelAdmin):
    list_display = \
        'equipment_unique_type_group', \
        'to_date', \
        'equipment_data_field', \
        'equipment_data_field_2', \
        'sample_correlation', \
        'last_updated'

    ordering = \
        'equipment_unique_type_group', \
        '-to_date', \
        '-sample_correlation'

    list_filter = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'to_date', \
        'equipment_data_field__name'

    list_select_related = \
        'equipment_unique_type_group', 'equipment_unique_type_group__equipment_general_type', \
        'equipment_data_field', 'equipment_data_field__equipment_general_type', 'equipment_data_field__equipment_data_field_type', \
        'equipment_data_field__data_type', 'equipment_data_field__numeric_measurement_unit', \
        'equipment_data_field_2', 'equipment_data_field_2__equipment_general_type', 'equipment_data_field_2__equipment_data_field_type', \
        'equipment_data_field_2__data_type', 'equipment_data_field_2__numeric_measurement_unit'

    show_full_result_count = False

    search_fields = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'equipment_data_field__name'

    readonly_fields = \
        'equipment_unique_type_group', \
        'to_date', \
        'equipment_data_field', \
        'equipment_data_field_2', \
        'sample_correlation', \
        'last_updated'

    @silk_profile(name='Admin: Equipment Unique Type Group Data Field Pairwise Correlations')
    def changelist_view(self, request, extra_context=None):
        return super(EquipmentUniqueTypeGroupDataFieldPairwiseCorrelationAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Equipment Unique Type Group Data Field Pairwise Correlation')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(EquipmentUniqueTypeGroupDataFieldPairwiseCorrelationAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    EquipmentUniqueTypeGroupDataFieldPairwiseCorrelation,
    admin_class=EquipmentUniqueTypeGroupDataFieldPairwiseCorrelationAdmin)


class EquipmentUniqueTypeGroupMonitoredDataFieldConfigStackedInline(StackedInline):
    model = EquipmentUniqueTypeGroupMonitoredDataFieldConfig

    fields = \
        'monitored_equipment_data_field', \
        'auto_included_numeric_equipment_data_fields', \
        'include_categorical_equipment_data_fields', \
        'manually_included_equipment_data_fields', \
        'manually_excluded_equipment_data_fields', \
        'active', \
        'comments'

    form = EquipmentUniqueTypeGroupMonitoredDataFieldConfigForm

    extra = 0

    def get_queryset(self, request):
        return super(EquipmentUniqueTypeGroupMonitoredDataFieldConfigStackedInline, self).get_queryset(request=request) \
            .select_related(
                'monitored_equipment_data_field',
                'monitored_equipment_data_field__equipment_general_type',
                'monitored_equipment_data_field__equipment_data_field_type',
                'monitored_equipment_data_field__data_type',
                'monitored_equipment_data_field__numeric_measurement_unit') \
            .prefetch_related(
                Prefetch(
                    lookup='excluded_equipment_data_fields',
                    queryset=
                        EquipmentDataField.objects
                        .select_related(
                            'equipment_general_type',
                            'equipment_data_field_type',
                            'data_type',
                            'numeric_measurement_unit')))


class EquipmentUniqueTypeGroupServiceConfigAdmin(ModelAdmin):
    list_display = \
        'equipment_unique_type_group', \
        'monitored_and_excluded_equipment_data_fields', \
        'active', \
        'from_date', \
        'to_date', \
        'configs', \
        'comments', \
        'last_updated'

    list_filter = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'active'

    show_full_result_count = False

    search_fields = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name',

    form = EquipmentUniqueTypeGroupServiceConfigForm

    inlines = EquipmentUniqueTypeGroupMonitoredDataFieldConfigStackedInline,

    def monitored_and_excluded_equipment_data_fields(self, obj):
        return '{}{}'.format(
            '; '.join(
                '{}{}'.format(
                    equipment_unique_type_group_monitored_data_field_config.monitored_equipment_data_field.name.upper(),
                    ' (excl: {})'.format(
                        ', '.join(excluded_equipment_data_field.name
                                  for excluded_equipment_data_field in
                                    equipment_unique_type_group_monitored_data_field_config.excluded_equipment_data_fields.all()))
                        if equipment_unique_type_group_monitored_data_field_config.excluded_equipment_data_fields.count()
                        else '')
                for equipment_unique_type_group_monitored_data_field_config in
                    obj.equipment_unique_type_group_monitored_data_field_configs.all()
                if equipment_unique_type_group_monitored_data_field_config.active),
            ' | global excl: {}'.format(
                ', '.join(excluded_equipment_data_field.name
                          for excluded_equipment_data_field in obj.global_excluded_equipment_data_fields.all()))
                if obj.global_excluded_equipment_data_fields.count()
                else '')

    def get_queryset(self, request):
        return super(EquipmentUniqueTypeGroupServiceConfigAdmin, self).get_queryset(request=request) \
            .select_related(
                'equipment_unique_type_group', 'equipment_unique_type_group__equipment_general_type') \
            .prefetch_related(
                Prefetch(
                    lookup='equipment_unique_type_group_monitored_data_field_configs',
                    queryset=
                        EquipmentUniqueTypeGroupMonitoredDataFieldConfig.objects
                        .select_related(
                            'monitored_equipment_data_field')
                        .prefetch_related(
                            'excluded_equipment_data_fields')),

                'global_excluded_equipment_data_fields')

    @silk_profile(name='Admin: Equipment Unique Type Group Service Configs')
    def changelist_view(self, request, extra_context=None):
        return super(EquipmentUniqueTypeGroupServiceConfigAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Equipment Unique Type Group Service Config')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(EquipmentUniqueTypeGroupServiceConfigAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    EquipmentUniqueTypeGroupServiceConfig,
    admin_class=EquipmentUniqueTypeGroupServiceConfigAdmin)


class BlueprintAdmin(ModelAdmin):
    list_display = \
        'equipment_unique_type_group', \
        'trained_to_date', \
        'uuid', \
        'timestamp', \
        'active', \
        'benchmark_metrics_summary', \
        'last_updated'

    list_filter = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'trained_to_date', \
        'timestamp', \
        'active'

    list_select_related = \
        'equipment_unique_type_group', \
        'equipment_unique_type_group__equipment_general_type'

    show_full_result_count = False

    search_fields = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'uuid'

    readonly_fields = \
        'equipment_unique_type_group', \
        'trained_to_date', \
        'uuid', \
        'timestamp', \
        'last_updated'

    def benchmark_metrics_summary(self, obj):
        if obj.benchmark_metrics:
            d = {}

            for label_var_name, benchmark_metrics in obj.benchmark_metrics.items():
                global_benchmark_metrics = benchmark_metrics['GLOBAL']

                good = True

                r2 = global_benchmark_metrics['R2']
                r2_text = '{:.1f}%'.format(100 * r2)
                if r2 < .68:
                    good = False
                    r2_text += ' (< 68%)'

                mae = global_benchmark_metrics['MAE']
                medae = global_benchmark_metrics['MedAE']
                mae_medae_ratio = mae / medae
                mae_medae_ratio_text = '{:.3g}x'.format(mae_medae_ratio)
                if mae_medae_ratio > 3:
                    good = False
                    mae_medae_ratio_text += ' (> 3x)'

                d[label_var_name.upper()
                  if good
                  else label_var_name] = \
                    dict(good=good,
                         R2_text=r2_text,
                         MAE=mae,
                         MedAE=medae,
                         MAE_MedAE_ratio_text=mae_medae_ratio_text)

            return '; '.join(
                '{}: R2 {}, MAE {:.3g} / MedAE {:.3g} = {}'.format(
                    k,
                    v['R2_text'],
                    v['MAE'],
                    v['MedAE'],
                    v['MAE_MedAE_ratio_text'])
                for k, v in sorted(d.items(), key=lambda i: i[1]['good'], reverse=True))

    @silk_profile(name='Admin: Blueprints')
    def changelist_view(self, request, extra_context=None):
        return super(BlueprintAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Blueprint')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(BlueprintAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    Blueprint,
    admin_class=BlueprintAdmin)


class EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileAdmin(ModelAdmin):
    list_display = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        'trained_to_date', \
        'n', \
        'r2', \
        'mae', \
        'medae', \
        'rmse', \
        'last_updated'

    list_filter = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'trained_to_date'

    list_select_related = \
        'equipment_unique_type_group', 'equipment_unique_type_group__equipment_general_type', \
        'equipment_data_field', 'equipment_data_field__equipment_general_type', 'equipment_data_field__equipment_data_field_type', \
                                'equipment_data_field__data_type', 'equipment_data_field__numeric_measurement_unit'

    show_full_result_count = False

    search_fields = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'equipment_data_field__name'

    readonly_fields = \
        'equipment_unique_type_group', \
        'equipment_data_field', \
        'trained_to_date', \
        'n', \
        'r2', \
        'mae', \
        'medae', \
        'rmse', \
        'last_updated'

    @silk_profile(name='Admin: Equipment Unique Type Group Data Field Blueprint Benchmark Metric Profiles')
    def changelist_view(self, request, extra_context=None):
        return super(EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Equipment Unique Type Group Data Field Blueprint Benchmark Metric Profile')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfile,
    admin_class=EquipmentUniqueTypeGroupDataFieldBlueprintBenchmarkMetricProfileAdmin)


class EquipmentInstanceDailyRiskScoreAdmin(ModelAdmin):
    list_display = \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'date', \
        'risk_score_value', \
        'last_updated'

    list_filter = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'risk_score_name', \
        'date'

    list_select_related = \
        'equipment_unique_type_group', 'equipment_unique_type_group__equipment_general_type', \
        'equipment_instance', 'equipment_instance__equipment_general_type', \
                              'equipment_instance__equipment_unique_type', 'equipment_instance__equipment_unique_type__equipment_general_type'

    readonly_fields = \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'date', \
        'risk_score_value', \
        'last_updated'

    show_full_result_count = False

    search_fields = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'equipment_instance__name', \
        'risk_score_name'

    @silk_profile(name='Admin: Equipment Instance Daily Risk Scores')
    def changelist_view(self, request, extra_context=None):
        return super(EquipmentInstanceDailyRiskScoreAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Equipment Instance Daily Risk Score')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(EquipmentInstanceDailyRiskScoreAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    EquipmentInstanceDailyRiskScore,
    admin_class=EquipmentInstanceDailyRiskScoreAdmin)


class EquipmentProblemTypeAdmin(ModelAdmin):
    list_display = 'name',

    show_full_result_count = False   # only a few, but skip counting anyway

    search_fields = 'name',

    @silk_profile(name='Admin: Equipment Problem Types')
    def changelist_view(self, request, extra_context=None):
        return super(EquipmentProblemTypeAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Equipment Problem Type')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(EquipmentProblemTypeAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    EquipmentProblemType,
    admin_class=EquipmentProblemTypeAdmin)


class EquipmentProblemDiagnosisAdmin(ModelAdmin):
    list_display = \
        'equipment_instance', \
        'from_date', \
        'to_date', \
        'duration', \
        'ongoing', \
        'equipment_problem_type_names', \
        'dismissed', \
        'comments', \
        'has_associated_alerts', \
        'last_updated'

    list_filter = \
        'equipment_instance__equipment_general_type__name', \
        'ongoing', \
        'from_date', \
        'to_date', \
        'dismissed'

    readonly_fields = \
        'date_range', \
        'duration', \
        'has_equipment_problems', \
        'has_associated_alerts', \
        'alerts'   # too many alerts, so Select box would freeze

    show_full_result_count = False

    search_fields = 'equipment_instance__name',

    form = EquipmentProblemDiagnosisForm

    def get_queryset(self, request):
        return super(EquipmentProblemDiagnosisAdmin, self).get_queryset(request) \
            .select_related(
                'equipment_instance', 'equipment_instance__equipment_general_type',
                'equipment_instance__equipment_unique_type', 'equipment_instance__equipment_unique_type__equipment_general_type') \
            .prefetch_related(
                'equipment_problem_types',
                Prefetch(
                    lookup='alerts',
                    queryset=
                        Alert.objects
                        .select_related(
                            'equipment_unique_type_group', 'equipment_unique_type_group__equipment_general_type',
                            'equipment_instance', 'equipment_instance__equipment_general_type',
                            'equipment_instance__equipment_unique_type', 'equipment_instance__equipment_unique_type__equipment_general_type',
                            'diagnosis_status')))

    def equipment_problem_type_names(self, obj):
        return ', '.join(equipment_problem_type.name
                         for equipment_problem_type in obj.equipment_problem_types.all())

    @silk_profile(name='Admin: Equipment Problem Diagnoses')
    def changelist_view(self, request, extra_context=None):
        return super(EquipmentProblemDiagnosisAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Equipment Problem Diagnosis')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(EquipmentProblemDiagnosisAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    EquipmentProblemDiagnosis,
    admin_class=EquipmentProblemDiagnosisAdmin)


class AlertAdmin(ModelAdmin):
    list_display = \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'threshold', \
        'from_date', \
        'to_date', \
        'duration', \
        'approx_average_risk_score', \
        'last_risk_score', \
        'cumulative_excess_risk_score', \
        'ongoing', \
        'diagnosis_status', \
        'has_associated_equipment_problem_diagnoses', \
        'last_updated'

    list_select_related = \
        'equipment_unique_type_group', 'equipment_unique_type_group__equipment_general_type', \
        'equipment_instance', 'equipment_instance__equipment_general_type', \
        'equipment_instance__equipment_unique_type', 'equipment_instance__equipment_unique_type__equipment_general_type', \
        'diagnosis_status'

    list_filter = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'risk_score_name', \
        'threshold', \
        'from_date', \
        'to_date', \
        'ongoing', \
        'diagnosis_status', \
        'has_associated_equipment_problem_diagnoses'

    show_full_result_count = False

    search_fields = \
        'equipment_unique_type_group__equipment_general_type__name', \
        'equipment_unique_type_group__name', \
        'equipment_instance__name', \
        'risk_score_name'

    form = AlertForm

    readonly_fields = \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'threshold', \
        'from_date', \
        'to_date', \
        'date_range', \
        'duration', \
        'approx_average_risk_score', \
        'last_risk_score', \
        'cumulative_excess_risk_score', \
        'ongoing', \
        'has_associated_equipment_problem_diagnoses', \
        'last_updated'

    @silk_profile(name='Admin: Alerts')
    def changelist_view(self, request, extra_context=None):
        return super(AlertAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Alert')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(AlertAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    Alert,
    admin_class=AlertAdmin)


class AlertDiagnosisStatusAdmin(ModelAdmin):
    list_display = \
        'index', \
        'name'

    show_full_result_count = False

    @silk_profile(name='Admin: Alert Diagnosis Statuses')
    def changelist_view(self, request, extra_context=None):
        return super(AlertDiagnosisStatusAdmin, self).changelist_view(
                request=request,
                extra_context=extra_context)

    @silk_profile(name='Admin: Alert Diagnosis Status')
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        return super(AlertDiagnosisStatusAdmin, self).changeform_view(
                request=request,
                object_id=object_id,
                form_url=form_url,
                extra_context=extra_context)


site.register(
    AlertDiagnosisStatus,
    admin_class=AlertDiagnosisStatusAdmin)
