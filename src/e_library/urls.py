from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django_otp.admin import OTPAdminSite
from django.utils.translation import gettext_lazy as _
# admin.site.__class__ = OTPAdminSite

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('system.urls')),
    path('', include('account.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    prefix_default_language=False
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

# handler400 = defaults.bad_request
# handler403 = defaults.permission_denied
# handler404 = defaults.page_not_found
# handler500 = defaults.server_error
