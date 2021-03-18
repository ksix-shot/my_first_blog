from django.urls import path
from . import views



urlpatterns = [
    path('vzsultanov7814.pythonanywhere.com', views.post_list, name='post_list'),
]