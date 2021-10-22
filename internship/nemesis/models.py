from django.db import models

# Create your models here.
class myuser(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.username