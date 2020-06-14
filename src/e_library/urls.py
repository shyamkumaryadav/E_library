from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from frontend.views import index
from account.admin import admin_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('op/', admin_site.urls),
    path('react/', index),
	path('', include('system.urls')),
    path('account/', include('account.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler400 = defaults.bad_request
# handler403 = defaults.permission_denied
# handler404 = defaults.page_not_found
# handler500 = defaults.server_error
