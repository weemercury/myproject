from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('order/<int:client_id>/', views.get_order, name='get_order'),
    path('product_form/<product_pk>/', views.product_form, name='product_form'),
]