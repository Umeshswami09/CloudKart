from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    address = models.TextField()

    city = models.CharField(max_length=100)

    payment_method = models.CharField(max_length=20)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name