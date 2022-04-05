from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.appointment_add, name='appointment_add'),
    path('update/<int:appointment_id>/', views.appointment_update, name='appointment_update'),
    path('appointments', views.appointment_show, name='appointment_show'),
    path('delete/<int:appointment_id>/', views.appointment_delete, name='appointment_delete'),
]
