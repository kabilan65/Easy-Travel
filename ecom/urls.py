from django.urls import path

from . import views

urlpatterns = [
    path('destinations/', views.destinations, name = 'destinations'),
    path('', views.index, name = 'index'),
]