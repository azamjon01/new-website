from django.urls import path
from .views import *

app_name = 'new'

urlpatterns = [
  path('', home, name="home"),
   
]