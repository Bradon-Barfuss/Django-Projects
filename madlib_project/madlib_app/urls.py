from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_madlib, name='create_madlib'),
]