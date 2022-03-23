from django.urls import path
from . import views

urlpatterns = [
    path('', views.decor, name='decor'),
]
