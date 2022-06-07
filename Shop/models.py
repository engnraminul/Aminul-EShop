from django.db import models

# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=30)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class Product(models.Model):
    Product_image = models.ImageField(upload_to='Products')
    Product_name = models.CharField(max_length=250)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    sort_details = models.TextField(max_length=300, verbose_name='sort_details')
    full_details = models.TextField(max_length=3000, verbose_name='full_details')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Product_name

    class Meta:
        ordering = ['-created_date']
