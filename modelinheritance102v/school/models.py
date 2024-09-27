from django.db import models

# Create your models here.
# parent
# -------------------------------------ABC------------------------------
class CommonInfo(models.Model):
    class Meta:
        abstract=True
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()

# child
class Student(CommonInfo):
    roll_no = models.IntegerField()
    fees = models.IntegerField()   
    date = None  # date field is not required.
    # by default abstract = False
# child
class Teacher(CommonInfo):
    subject = models.CharField(max_length=100)
    salary = models.IntegerField()
    # by default abstract= False
# child
class Contractor(CommonInfo):
    date = models.DateTimeField() #override
    payment = models.IntegerField()
    # by default abstract = False
# ------------------------------------------------------------------------------------------------------------------
# Multitable Inheritance.
class Parent(models.Model):
    pname= models.CharField(max_length=70)
    city = models.CharField(max_length=70)

class Child(Parent):
    sname = models.CharField(max_length=70)
    roll = models.IntegerField()
    
# --------------------------------------------------Proxy Model---------------------------
class ExamCenter(models.Model):
    cname = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    
class MyExamCenterProxy(ExamCenter):   # same data
    # there is no proxy table in db
    class Meta:
        proxy = True
        ordering = ['cname'] #['-cname'] # behaviour can be different.
        
