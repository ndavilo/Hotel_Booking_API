from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name      = models.CharField(max_length=100)
    middle_name     = models.CharField(max_length=100, null=True, blank=True)
    last_name       = models.CharField(max_length=100)
    phone_number    = models.CharField(max_length=15)
    email           = models.EmailField()
    address         = models.CharField(max_length=200)
    photo           = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.email

class Reservation(models.Model):
    room_number         = models.IntegerField(null=True, blank=True)
    room_type           = models.CharField(max_length=100)
    arrival_date        = models.DateField()
    total_nights        = models.IntegerField()
    special_request     = models.CharField(max_length=200, null=True, blank=True)
    payment_method      = models.CharField(max_length=100)
    payment_validation  = models.ImageField(null=True, blank=True)
    customer_id         = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.arrival_date +' '+ self.room_type

