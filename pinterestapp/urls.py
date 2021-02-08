from django.urls import path
from . import views

# ADD URLS OF THIS APP
urlpatterns = [
    path('', views.index, name='index'),
]