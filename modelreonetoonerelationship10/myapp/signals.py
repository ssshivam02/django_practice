from django.db.models.signals import post_delete
from myapp.models import Page
from django.dispatch import receiver

@receiver(post_delete, sender = Page)
def delete_related_user(sender, instance, **kwargs):
    print("Page Post_Delete")
    instance.user.delete()