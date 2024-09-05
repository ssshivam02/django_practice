from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender, user, request, **kwargs):
    print("-------------------")
    print("Logged-in Signal.....")
    print("Sender:", sender)
    print("Request:", request)
    print("USER:", user)
    print("Userpassword:", user.password)
    print(f'Kwargs:{kwargs}')
    
# user_logged_in.connect(login_success, sender=User) # in place of decorator we can use this line also.

@receiver(user_logged_out,sender=User)
def log_out(sender, user, request, **kwargs):
    print("-------------------")
    print("Logged-out Signal.....")
    print("Sender:", sender)
    print("Request:", request)
    print("USER:", user)
    print("Userpassword:", user.password)
    print(f'Kwargs:{kwargs}')
    
@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print("-------------------")
    print("Login Failed -Signal.....")
    print("Sender:", sender)
    print("Request:", request)
    print("credentails:", credentials)
    print(f'Kwargs:{kwargs}')
    