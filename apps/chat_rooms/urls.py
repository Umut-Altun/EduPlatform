from django.urls import path
from . import views

app_name = 'chat_rooms'

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('create/', views.create_room, name='create_room'),
    path('room/<int:room_id>/', views.chat_room, name='chat_room'),
]
