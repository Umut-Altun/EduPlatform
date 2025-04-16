from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import index, login_view, register_view, logout_view

# Django projesinin URL yapılandırması. URL'leri ve bunlara karşılık gelen görünümleri tanımlar.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),  # Ana sayfa için 'home' adı veriyoruz
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('icerik-paylasimi/', include('apps.content_sharing.urls')),
    path('ayarlar/', include('apps.settings.urls')),
]

# Medya dosyalarını geliştirme aşamasında sunun
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
