from django.db import models
from django.contrib.auth.models import User
# Create your models here.ma

# only one page ---- one user
class Page(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key =True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key =True, limit_choices_to={'is_staff':True}) #is_staff is for limiting.
    page_name = models.CharField(max_length=70)
    page_cat = models.CharField(max_length=70)
    page_publish_date = models.DateField()
    

# if we delete one page then user not delete in above case.
# models.PROTECT is for protecting user in deleting page.
# user delete than page also get deleted.
# page delete then user not get deleted.

# for deleting page with user, we using signal
