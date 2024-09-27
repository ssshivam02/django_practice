from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    #if user get deleted then Post also got deleted.
    # user= models.ForeignKey(User, on_delete= models.CASCADE)
    # for protect if any post is present then dont delete user.
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post_title = models.CharField(max_length=70)
    post_cat = models.CharField(max_length=70)
    post_publish_date = models.DateField()