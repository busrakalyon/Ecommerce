from django.db import models

class Customer(models.Model):

    Lastname = models.CharField(max_length=255)

    Firstname = models.CharField(max_length=255)

    email = models.EmailField(max_length=255)

    phoneNmuber = models.IntegerField()

    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"


class Product(models.Model):
    name = models.CharField(max_length=255)  # Ürün adı
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Fiyat
    description = models.TextField()  # Ürün açıklaması
    stock = models.IntegerField()  # Stok miktarı
    created_at = models.DateTimeField(auto_now_add=True)  # Ürün eklenme tarihi

    def __str__(self):
        return self.name
    