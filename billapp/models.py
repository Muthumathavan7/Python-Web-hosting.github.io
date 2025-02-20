
# from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     product_id = models.CharField(max_length=100, unique=True)
#     available_stocks = models.IntegerField()
#     price = models.FloatField()
#     tax_percentage = models.FloatField()

#     def __str__(self):
#         return self.name

# class Purchase(models.Model):
#     customer_email = models.EmailField()
#     total_amount = models.FloatField(null=True)
#     paid_amount = models.FloatField(null=True)
#     balance_amount = models.FloatField(null=True)
#     timestamp = models.DateTimeField(auto_now_add=True)

# class PurchaseItem(models.Model):
#     purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     subtotal = models.FloatField()

# # Create your models here.
from django.db import models

class Customer(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=255)
    product_id = models.CharField(max_length=50, unique=True)
    available_stock = models.IntegerField()
    price = models.FloatField()
    tax_percentage = models.FloatField()

    def __str__(self):
        return self.name

class Purchase(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField()

    def __str__(self):
        return f"Purchase {self.id} by {self.customer.email}"

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    tax = models.FloatField()

class Denomination(models.Model):
    value = models.IntegerField(unique=True)
    count = models.IntegerField()

    def __str__(self):
        return f"{self.value} x {self.count}"
