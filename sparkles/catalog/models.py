from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from slugify import slugify
from uuid import uuid4


User = get_user_model()


class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Фрукты', 'Фрукты'),
        ('Овощи', 'Овощи'),
        ('Мясо', 'Мясо'),
        ('Напитки', 'Напитки'),
    ]
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name

    #def get_absolute_url(self):


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', verbose_name='Категория')
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')
    slug = models.SlugField(unique=True, blank=True, verbose_name='Идентификатор')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    description = models.TextField(blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='catalog/products/', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.name)
            while Product.objects.filter(slug=slug).exists():
                slug += '-' + str(uuid4())[:3]
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('catalog:product_detail', kwargs={'product_slug': self.slug})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    name = models.CharField(max_length=50, verbose_name='Краткое описание комментария')
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания комментария')

    def __str__(self):
        return self.name
