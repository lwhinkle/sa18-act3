from django.urls import path
from . import views

urlpatterns = [
    path('products/<int: id>/', views.product_show, name = 'product_show'),
]