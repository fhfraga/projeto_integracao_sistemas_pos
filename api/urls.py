from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.ListProducts.as_view())
]