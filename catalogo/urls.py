from django.urls import path #cambio desde django 2.0
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]