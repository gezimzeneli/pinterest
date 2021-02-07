from django.urls import path
from . import views         # . means from current folder

urlpatterns = [
    path('', views.index),
]