from django import forms

from users.forms import CustomBaseForm
from .models import Product, Category


class CreateProductForm(forms.ModelForm, CustomBaseForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Product
        fields = ['category', 'name', 'price', 'description', 'image']
