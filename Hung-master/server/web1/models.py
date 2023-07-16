from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    add =models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    mail=models.EmailField()
    def __str__(self):
        return self.name