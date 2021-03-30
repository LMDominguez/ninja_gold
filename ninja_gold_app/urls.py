from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get_farm', views.get_farm),
    path('get_cave', views.get_cave),
    path('get_house', views.get_house),
    path('get_casino', views.get_casino),
    path('process_money', views.process_money)
]
