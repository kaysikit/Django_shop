from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категории"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField("Наименование товара", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=9, decimal_places=2)
    quantity= models.PositiveIntegerField("Количество", default=0)
    image = models.ImageField("Изображение товара", upload_to='products_images')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"
