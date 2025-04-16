from django.urls import path
from . import views

app_name = 'settings'

urlpatterns = [
    path('', views.settings_home, name='home'),
    path('profil/', views.profile_settings, name='profile'),
    path('sifre/', views.password_settings, name='password'),
    path('gonderilerim/', views.user_content, name='my_content'),
]
