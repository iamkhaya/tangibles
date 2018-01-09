from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /orders/
    path('order/', views.order, name='order'),
    # ex: /products/
    path('product/', views.product, name='product'),
    # ex: /users/
    path('user/', views.user, name='user'),
]
