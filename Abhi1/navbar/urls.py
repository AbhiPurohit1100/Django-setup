
from django.urls import path

from . import views
urlpatterns = [
    path('', views.homenav, name='homenav'),# default adress /navbar
    path('size/', views.size, name="size") 
]