from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import get_object_or_404

from .models import Product, Category, Comment


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        if self.request.GET.get('category') != 'none':
            return Product.objects.filter(category__id=self.request.GET.get('category'))
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Список товаров'
        context['category_list'] = Category.objects.all()
        try:
            context['current_category'] = int(self.request.GET.get('category'))
        except:
            context['current_category'] = 'none'
        return context


class ProductDetailView(DetailView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'


class ProductCreateView(CreateView):
    model = Product
