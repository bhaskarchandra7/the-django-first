from django.db import models

# Create your models here.
from django.db import models

class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.name