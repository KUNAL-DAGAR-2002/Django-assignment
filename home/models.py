from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.CharField(max_length=100)
    order_value = models.IntegerField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_date = models.CharField(max_length=11)

    def __str__(self):
        return self.order_id
