from django.dispatch import Signal,receiver

# creating signals
notification = Signal(providing_args=['request','user'])


#receiver function
@receiver(notification)
def send_notification(sender, **kwargs):
    print(sender)
    print(f'{kwargs}')
    print("Notification")