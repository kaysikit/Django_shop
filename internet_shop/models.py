from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(name='Наименование товара', max_length=255)
    description = models.TextField(name='Описание')
    price = models.DecimalField(name='Цена', max_digits=9, decimal_places=2)
    quantity= models.PositiveIntegerField(name='Количество', default=0)
    image = models.ImageField(name='Изображение товара', upload_to='products_images')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"