from django.contrib.admin import ModelAdmin, site

from .models import Blueprint, Alert


class BlueprintAdmin(ModelAdmin):
    list_display = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'trained_to_date', \
        'timestamp', \
        'uuid', \
        'active'

    list_filter = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'trained_to_date', \
        'timestamp', \
        'active'

    list_select_related = \
        'equipment_general_type', \
        'equipment_unique_type_group'

    show_full_result_count = False

    search_fields = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'uuid'


site.register(
    Blueprint,
    admin_class=BlueprintAdmin)


class AlertAdmin(ModelAdmin):
    list_display = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name', \
        'threshold', \
        'from_date', \
        'to_date', \
        'quantified_risk_degree', \
        'active'

    list_select_related = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'equipment_instance'

    list_filter = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'risk_score_name', \
        'threshold', \
        'from_date', \
        'to_date', \
        'active', \
        'equipment_instance'

    show_full_result_count = False

    search_fields = \
        'equipment_general_type', \
        'equipment_unique_type_group', \
        'equipment_instance', \
        'risk_score_name'


site.register(
    Alert,
    admin_class=AlertAdmin)
