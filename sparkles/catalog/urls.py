from django.urls import path

from .views import ProductListView, ProductDetailView

app_name = 'catalog'

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail')
]

