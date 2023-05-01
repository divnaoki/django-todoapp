from django.urls import path
from . import views
from .views import index, craete_todo

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.craete_todo, name='craete_todo'),
]