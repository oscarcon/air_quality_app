from django.urls import path

from . import views

app_name = 'current'
urlpatterns = [
    path('', views.current_data, name='current')
]