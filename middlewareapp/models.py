from django.db import models

# Create your models here.
class Customer(models.Model):
    customerName = models.CharField(max_length=50)
    creditLimit = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=50)

    class Meta:  
        db_table = "customers"
