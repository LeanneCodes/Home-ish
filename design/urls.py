from django.urls import path
from . import views

urlpatterns = [
    path('', views.design, name='design'),
    path('design_show/', views.design_show, name='design_show'),
    path('design_update/<item_id>/', views.design_update, name='design_update'),
    path('design_delete/<item_id>/', views.design_delete, name='design_delete'),
]
