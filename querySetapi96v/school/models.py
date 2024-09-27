from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    roll = models.IntegerField(unique=True, null = False)
    marks = models.IntegerField()
    pass_date = models.DateField()
    
