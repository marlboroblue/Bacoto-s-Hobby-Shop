from django.db import models


# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    phone = models.IntegerField()
    email = models.EmailField(max_length=250, blank=True)
    address = models.CharField(max_length=250)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, default=1)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.product_name


class Order(models.Model):
    
    product_name = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    address = models.CharField(max_length=250, null=True)
    phone = models.IntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} {self.product_name} {self.date}  '
