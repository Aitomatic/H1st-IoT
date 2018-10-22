from django.db.models import Prefetch
from django.http import HttpResponse, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token

from rest_framework.authentication import \
    BasicAuthentication, RemoteUserAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.decorators import action, api_view
from rest_framework.generics import GenericAPIView, \
    ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
    ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import \
    ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.pagination import CursorPagination, LimitOffsetPagination, PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import CoreJSONRenderer, JSONRenderer, \
    HTMLFormRenderer, StaticHTMLRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.status import \
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet, ReadOnlyModelViewSet

from silk.profiling.profiler import silk_profile

from .filters import \
    DataTypeFilter, \
    NumericMeasurementUnitFilter, \
    EquipmentDataFieldTypeFilter, \
    EquipmentGeneralTypeFilter, \
    EquipmentDataFieldFilter, \
    EquipmentUniqueTypeGroupFilter, \
    EquipmentUniqueTypeFilter, \
    EquipmentFacilityFilter, \
    EquipmentInstanceFilter, \
    EquipmentSystemFilter
from .models import \
    DataType, \
    NumericMeasurementUnit, \
    EquipmentDataFieldType, \
    EquipmentGeneralType, \
    EquipmentDataField, \
    EquipmentUniqueTypeGroup, \
    EquipmentUniqueType, \
    EquipmentFacility, \
    EquipmentInstance, \
    EquipmentSystem
from .serializers import \
    DataTypeSerializer, \
    NumericMeasurementUnitSerializer, \
    EquipmentDataFieldTypeSerializer, \
    EquipmentGeneralTypeSerializer, \
    EquipmentDataFieldSerializer, \
    EquipmentUniqueTypeGroupSerializer, \
    EquipmentUniqueTypeSerializer, \
    EquipmentFacilitySerializer, \
    EquipmentInstanceSerializer, \
    EquipmentSystemSerializer


class DataTypeViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` an unfiltered, unpaginated list of 2 Data Types named "cat" and "num"

    retrieve:
    `GET` the Data Type specified by `name` "cat" or "num"
    """
    queryset = DataType.objects.all()

    serializer_class = DataTypeSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticatedOrReadOnly,

    lookup_field = 'name'

    lookup_url_kwarg = 'data_type_name___cat_or_num'

    filter_class = pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer


class NumericMeasurementUnitViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, unpaginated list of Numeric Measurement Units

    retrieve:
    `GET` the Numeric Measurement Unit specified by `name`

    create:
    `POST` a new Numeric Measurement Unit by `name`

    update:
    `PUT` updated data for the Numeric Measurement Unit specified by `name`

    partial_update:
    `PATCH` the Numeric Measurement Unit specified by `name`

    destroy:
    `DELETE` the Numeric Measurement Unit specified by `name`
    """
    queryset = NumericMeasurementUnit.objects.all()

    serializer_class = NumericMeasurementUnitSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticatedOrReadOnly,

    lookup_field = 'name'

    lookup_url_kwarg = 'numeric_measurement_unit_name'

    filter_class = NumericMeasurementUnitFilter

    pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer


class EquipmentDataFieldTypeViewSet(ReadOnlyModelViewSet):
    """
    list:
    `GET` an unfiltered, unpaginated list of 2 Equipment Data Field Types named "control" and "measure"

    retrieve:
    `GET` the Equipment Data Field Type specified by `name` "control" or "measure"
    """
    queryset = EquipmentDataFieldType.objects.all()

    serializer_class = EquipmentDataFieldTypeSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticatedOrReadOnly,

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_data_field_type_name___control_or_measure'

    filter_class = pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer


class EquipmentGeneralTypeViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, non-paginated list of Equipment General Types

    retrieve:
    `GET` the Equipment General Type specified by `name`

    create:
    `POST` a new Equipment General Type by `name`

    update:
    `PUT` updated data for the Equipment General Type specified by `name`

    partial_update:
    `PATCH` the Equipment General Type specified by `name`

    destroy:
    `DELETE` the Equipment General Type specified by `name`
    """
    queryset = EquipmentGeneralType.objects.all()

    serializer_class = EquipmentGeneralTypeSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_general_type_name'

    filter_class = EquipmentGeneralTypeFilter

    pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer


class EquipmentDataFieldViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, non-paginated list of Equipment Data Fields

    retrieve:
    `GET` the Equipment Data Field specified by `id`

    create:
    `POST` a new Equipment Data Field

    update:
    `PUT` updated data for the Equipment Data Field specified by `id`

    partial_update:
    `PATCH` the Equipment Data Field specified by `id`

    destroy:
    `DELETE` the Equipment Data Field specified by `id`
    """
    queryset = \
        EquipmentDataField.objects \
        .select_related(
            'equipment_general_type',
            'equipment_data_field_type',
            'data_type',
            'numeric_measurement_unit') \
        .prefetch_related(
            Prefetch(
                'equipment_unique_types',
                queryset=EquipmentUniqueType.objects.select_related('equipment_general_type')))

    serializer_class = EquipmentDataFieldSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    filter_class = EquipmentDataFieldFilter

    pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='Equipment Data Fields')
    def list(self, request, *args, **kwargs):
        return super(EquipmentDataFieldViewSet, self).list(request, *args, **kwargs)


class EquipmentUniqueTypeGroupViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, non-paginated list of Equipment Unique Type Groups

    retrieve:
    `GET` the Equipment Unique Type Group specified by `name`

    create:
    `POST` a new Equipment Unique Type Group

    update:
    `PUT` updated data for the Equipment Unique Type Group specified by `name`

    partial_update:
    `PATCH` the Equipment Unique Type Group specified by `name`

    destroy:
    `DELETE` the Equipment Unique Type Group specified by `name`
    """
    queryset = \
        EquipmentUniqueTypeGroup.objects \
        .select_related(
            'equipment_general_type') \
        .prefetch_related(
            Prefetch(
                'equipment_unique_types',
                queryset=EquipmentUniqueType.objects.select_related('equipment_general_type')),
            Prefetch(
                'equipment_data_fields',
                queryset=EquipmentDataField.objects.select_related('equipment_general_type', 'equipment_data_field_type')))

    serializer_class = EquipmentUniqueTypeGroupSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_unique_type_group_name'

    filter_class = EquipmentUniqueTypeGroupFilter

    pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='Equipment Unique Type Groups')
    def list(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeGroupViewSet, self).list(request, *args, **kwargs)


class EquipmentUniqueTypeViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, non-paginated list of Equipment Unique Types

    retrieve:
    `GET` the Equipment Unique Type specified by `id`

    create:
    `POST` a new Equipment Unique Type

    update:
    `PUT` updated data for the Equipment Unique Type specified by `id`

    partial_update:
    `PATCH` the Equipment Unique Type specified by `id`

    destroy:
    `DELETE` the Equipment Unique Type specified by `id`
    """
    queryset = \
        EquipmentUniqueType.objects \
        .select_related(
            'equipment_general_type') \
        .prefetch_related(
            Prefetch(
                'data_fields',
                queryset=EquipmentDataField.objects.select_related('equipment_general_type', 'equipment_data_field_type')),
            Prefetch(
                'groups',
                queryset=EquipmentUniqueTypeGroup.objects.select_related('equipment_general_type')))

    serializer_class = EquipmentUniqueTypeSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    filter_class = EquipmentUniqueTypeFilter

    pagination_class = None

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='Equipment Unique Types')
    def list(self, request, *args, **kwargs):
        return super(EquipmentUniqueTypeViewSet, self).list(request, *args, **kwargs)


class EquipmentFacilityViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Equipment Facilities

    retrieve:
    `GET` the Equipment Facility specified by `name`

    create:
    `POST` a new Equipment Facility

    update:
    `PUT` updated data for the Equipment Facility specified by `name`

    partial_update:
    `PATCH` the Equipment Facility specified by `name`

    destroy:
    `DELETE` the Equipment Facility specified by `name`
    """
    queryset = \
        EquipmentFacility.objects \
        .prefetch_related(
            'equipment_instances')

    serializer_class = EquipmentFacilitySerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_facility_name'

    filter_class = EquipmentFacilityFilter

    pagination_class = LimitOffsetPagination

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='Equipment Facilities')
    def list(self, request, *args, **kwargs):
        return super(EquipmentFacilityViewSet, self).list(request, *args, **kwargs)


class EquipmentInstanceViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Equipment Instances

    retrieve:
    `GET` the Equipment Instance specified by `name`

    create:
    `POST` a new Equipment Instance

    update:
    `PUT` updated data for the Equipment Instance specified by `name`

    partial_update:
    `PATCH` the Equipment Instance specified by `name`

    destroy:
    `DELETE` the Equipment Instance specified by `name`
    """
    queryset = \
        EquipmentInstance.objects \
        .select_related(
            'equipment_general_type',
            'equipment_unique_type', 'equipment_unique_type__equipment_general_type',
            'equipment_facility')

    serializer_class = EquipmentInstanceSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    lookup_field = 'name'

    lookup_url_kwarg = 'equipment_instance_name'

    filter_class = EquipmentInstanceFilter

    pagination_class = LimitOffsetPagination

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='Equipment Instances')
    def list(self, request, *args, **kwargs):
        return super(EquipmentInstanceViewSet, self).list(request, *args, **kwargs)


class EquipmentSystemViewSet(ModelViewSet):
    """
    list:
    `GET` a filterable, paginated list of Equipment Systems

    retrieve:
    `GET` the Equipment System specified by `id`

    create:
    `POST` a new Equipment System

    update:
    `PUT` updated data for the Equipment System specified by `id`

    partial_update:
    `PATCH` the Equipment System specified by `id`

    destroy:
    `DELETE` the Equipment System specified by `id`
    """
    queryset = \
        EquipmentSystem.objects \
        .select_related(
            'equipment_facility') \
        .prefetch_related(
            'equipment_instances')

    serializer_class = EquipmentSystemSerializer

    authentication_classes = \
        BasicAuthentication, \
        RemoteUserAuthentication, \
        SessionAuthentication, \
        TokenAuthentication

    permission_classes = IsAuthenticated,

    filter_class = EquipmentSystemFilter

    pagination_class = LimitOffsetPagination

    renderer_classes = \
        CoreJSONRenderer, \
        JSONRenderer

    @silk_profile(name='Equipment Systems')
    def list(self, request, *args, **kwargs):
        return super(EquipmentSystemViewSet, self).list(request, *args, **kwargs)


# request.data
# Response(serializer.data, status=HTTP_201_CREATED)
# Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
