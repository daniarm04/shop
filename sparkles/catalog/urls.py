from django.urls import path

from .views import ProductListView, ProductDetailView, ProductCreateView

app_name = 'catalog'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
]

