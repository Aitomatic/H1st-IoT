"""H1st IoT URLs."""


from django.urls.conf import include, path
from django.contrib import admin
from django.views.generic.base import RedirectView

from h1st_iot.data_mgmt.base.urls import URL_PATTERNS as BASE_URLS
from h1st_iot.data_mgmt.maint_ops.urls import URL_PATTERNS as MAINT_OPS_URLS


admin.site.index_title = 'H1st'
admin.site.site_title = 'IoT'
admin.site.site_header = 'H1st IoT'


urlpatterns = [
    # Home URL Redirected to Admin
    path('', RedirectView.as_view(url='/admin')),
    path('admin/', admin.site.urls),

    # API URLs
    path('api/auth/',
         include('rest_framework.urls', namespace='rest_framework')),

    # Silk Profiling URLs
    path('silk/',
         include('silk.urls', namespace='silk'))

] + BASE_URLS + MAINT_OPS_URLS
