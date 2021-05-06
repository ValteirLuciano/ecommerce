from django.urls import path
from .views import ProductListView, ProductDetailView


urlpatterns = [
    path('products/', ProductListView.as_view(), name='list'),
    path('products/<int:pk>', ProductDetailView.as_view(), name=''),
]
