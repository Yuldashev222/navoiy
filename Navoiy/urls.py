from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Base.urls')),
    path('devon/', include('Devon.urls')),
    path('asar/', include('Asar.urls')),
    path('gazal', include('Gazal.urls')),
    path('sheriy_sanat/', include('Sheriy_sanat.urls')),
    path('maqol_ibora/', include('Maqol_Ibora.urls')),
    path('search/', include('Search.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('arxa_ist/', include('Arzaizm_istorizm.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
