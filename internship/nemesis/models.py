from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey



# Create your models here.
class myuser(models.Model):
    username = models.CharField(max_length=30)
    phone = models.CharField(max_length=12,default='NA')
    email = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
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
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    user_id_id = models.IntegerField(default=1)
    name = models.CharField(max_length=100)
    heading = models.CharField(max_length=500)
    verification_status = models.CharField(max_length=100, default="Not Verified")
    description = models.CharField(max_length=1500)
    mobile_id = models.ForeignKey(mobile_details,on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    def __str__(self):
        return self.name


# class reviews1(models.Model):
#     user_id = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
#     name = models.CharField(max_length=100)
#     heading = models.CharField(max_length=500)
#     verification_status = models.CharField(max_length=100)
#     description = models.CharField(max_length=1500)
#     mobile_id = models.ForeignKey(mobile_details,on_delete=models.CASCADE)
#     is_verified = models.BooleanField(default=False)
#     def __str__(self):
#         return self.name