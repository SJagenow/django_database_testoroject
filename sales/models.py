from django.db import models

# Create your models here.
#many
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_adress = models.CharField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)
#one
class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    #many-to-many Order


class Bill(models.Model):
     total_amount = models.FloatField()
     is_paid = models.BooleanField(default=False)
            # one_to_one Order 


class Order(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="Producttype")
    bill = models.OneToOneField(Bill, on_delete=models.CASCADE)

class Producttype(models.Model):
    order = models.ForeignKey(Order,on_delete=models.Cascade)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_name = models.CharField(max_length=300)
    
