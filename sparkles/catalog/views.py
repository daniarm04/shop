from django.views.generic import ListView, DetailView, CreateView

from .models import Product, Category, Comment
from .forms import CreateProductForm


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        category = self.get_current_category()
        if category != 'Все категории':
            return Product.objects.filter(category__name=category)
        return super().get_queryset()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['category_list'] = Category.objects.all()
        context['current_category'] = self.get_current_category()
        return context

    def get_current_category(self):
        if self.request.GET.get('category') and self.request.GET.get('category') != 'Все категории':
            return self.request.GET.get('category')
        return 'Все категории'


class ProductDetailView(DetailView):
    model = Product
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'catalog/product_create.html'
    form_class = CreateProductForm
