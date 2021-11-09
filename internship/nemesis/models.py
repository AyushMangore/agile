from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class myuser(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username

class mobile_details(models.Model):
    mob_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=2,decimal_places=1)
    price = models.IntegerField()
    image_link = models.URLField(max_length = 500)
    product_link = models.URLField(max_length = 500)
    def __str__(self):
        return self.name

class reviews(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    heading = models.CharField(max_length=500)
    verification_status = models.CharField(max_length=100)
    description = models.CharField(max_length=1500)
    mobile_id = models.ForeignKey(mobile_details,on_delete=models.CASCADE)
    def __str__(self):
        return self.name