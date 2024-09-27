from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete,pre_init,pre_save,post_delete,post_init,post_save, pre_migrate, post_migrate
from django.core.signals import request_finished, request_started,got_request_exception
from django.db.backends.signals import connection_created

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

# before save method sender = modelclass
@receiver(pre_save, sender= User)
def at_beginning_save(sender, instance, **kwargs):
    print("-------------------")
    print("Pre save -Signal.....")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs:{kwargs}')
    
@receiver(post_save, sender= User)
def at_ending_save(sender, created,instance, **kwargs):
    if created: # for new user
        print("-------------------")
        print("Post save -Signal.....")
        print('New Record')
        print("Sender:", sender)
        print('created',created)
        print("Instance:", instance)
        print(f'Kwargs:{kwargs}')
    else: # for update existing user.
        print("-------------------")
        print("Post save -Signal.....")
        print("Update")
        print("Sender:", sender)
        print('created',created)
        print("Instance:", instance)
        print(f'Kwargs:{kwargs}')
        

@receiver(pre_delete, sender= User)
def at_beginning_delete(sender, instance, **kwargs):
    print("-------------------")
    print("Pre delete -Signal.....")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs:{kwargs}')
    
@receiver(post_delete, sender= User)
def at_ending_delete(sender, instance, **kwargs):
    print("-------------------")
    print("Post delete -Signal.....")
    print("Sender:", sender)
    print("Instance:", instance)
    print(f'Kwargs:{kwargs}')


# when we save below will run
@receiver(pre_init, sender= User)
def at_beginning_init(sender,*args,**kwargs):
    print("-------------------")
    print("Pre Init -Signal.....")
    print("Sender:", sender)
    print(f"Args: {args}")
    print(f'Kwargs:{kwargs}')
    
@receiver(post_init, sender= User)
def at_ending_init(sender, *args, **kwargs):
    print("-------------------")
    print("Post init -Signal.....")
    print("Sender:", sender)
    print(f"Args: {args}")
    print(f'Kwargs:{kwargs}')
    
@receiver(request_started)
def at_beginning_request(sender,environ, **kwargs):
    print("-------------------")
    print("At Beginning Request.....")
    print("Sender:", sender)
    print(f"Environ: {environ}")
    print(f'Kwargs:{kwargs}')

@receiver(request_finished)
def at_ending_request(sender,**kwargs):
    print("-------------------")
    print("At Beginning Request.....")
    print("Sender:", sender)
    print(f'Kwargs:{kwargs}')
    
@receiver(got_request_exception)
def at_req_exception(sender, request,**kwargs):
    print("-------------------")
    print("At Request Exception.....")
    print("Sender:", sender)
    print('Request:', request)
    print(f'Kwargs:{kwargs}')
    
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print("-------------------")
    print("Before install app.....")
    print("Sender:", sender)
    print('App_config', app_config)
    print('Verbosity', verbosity)
    print('Interactive', interactive)
    print('Using', using)
    print('Plan', plan)
    print('App', apps)
    print(f'Kwargs:{kwargs}')
    
@receiver(post_migrate)
def after_install_app(sender, app_config, verbosity, interactive, using, plan, apps,**kwargs):
    print("-------------------")
    print("After install app.....")
    print("Sender:", sender)
    print('App_config', app_config)
    print('Verbosity', verbosity)
    print('Interactive', interactive)
    print('Using', using)
    print('Plan', plan)
    print('App', apps)
    print(f'Kwargs:{kwargs}')

@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print("---------------------------------------")
    print("Initial connection to the database................")
    print('Sender:', sender)
    print('connection:', connection)
    print(f'Kwargs:{kwargs}')