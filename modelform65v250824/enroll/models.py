from django.db import models

# Create your models here.
class Students(models.Model):
    stuid = models.IntegerField(primary_key=True)
    stuname = models.CharField(max_length=70)
    stuemail = models.EmailField(max_length=70)
    stupass = models.CharField(max_length=70)
    comment = models.CharField(max_length=40, default="Not required")
    
    # this is not required when we using modeladmin for table
    # def __str__(self):
    #     return str(self.stuname)
class User(models.Model):
    name = models.CharField(max_length=70,) #blank = True) #blank makes name as optional field
    email= models.EmailField(max_length=254)
    password = models.CharField(max_length=70)
    