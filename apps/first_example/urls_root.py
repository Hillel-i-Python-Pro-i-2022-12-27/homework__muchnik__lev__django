from django.urls import path
from apps.first_example import views

app_name = "root"

urlpatterns = [
     path('', views.index, name='index'),
]