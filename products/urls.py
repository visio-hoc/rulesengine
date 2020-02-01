from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='product-home'),
    path('extended/', views.extended, name='product-extended'),
]
