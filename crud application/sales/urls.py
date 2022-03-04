from django.conf.urls import url, include
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='dashboard'),
    path('add/', views.add, name='add_sales_record'),
    path('edit/<id>', views.edit, name='edit_sales_record')
]