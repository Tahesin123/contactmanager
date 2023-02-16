from django.db import models

# Create your models here.
class Contact(models.Model):
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    work=models.CharField(max_length=200)
    phone=models.IntegerField()
    description=models.CharField(max_length=500)
    profileImage=models.ImageField(upload_to="image/",null=True, blank=True)