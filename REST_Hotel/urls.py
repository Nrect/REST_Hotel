from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

urlpatterns = [path('admin/', admin.site.urls),
               path('auth/', include('djoser.urls')),
               path('auth/', include('djoser.urls.authtoken')),
               # path('auth/', include('djoser.urls.jwt')),
               path('api/v1/', include('api.urls')),

               path('', include('backend.hotel.urls'))
               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)), ] + urlpatterns
