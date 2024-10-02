from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_adress = models.CharField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)

class Order(models.Model):
    #many-to-one Customer
    #one-to-one Bill
    pass

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    #many-to-many Order

    class Bill(models.Model):
     total_amount = models.FloatField()
     is_paid = models.BooleanField(default=False)
            # one_to_one Order 
