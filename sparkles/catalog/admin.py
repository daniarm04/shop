from django.contrib import admin

from .models import Product, Category, Comment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'slug']
    fields = ['name', 'category', 'price', 'description', 'image']
    ordering = ['name', 'category']
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'product', 'name']
    ordering = ['created_at']
    search_fields = ['author', 'product', 'name']
