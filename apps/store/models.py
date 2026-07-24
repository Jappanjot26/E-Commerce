from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Product(models.Model):
    # add ref to Category model indexed to 'products' and on delete it should cascade those category products as well
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    # blank and null is allowed
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()

    def __str__(self):
        return self.title