from django.apps import AppConfig


class MiniblogConfig(AppConfig):
    name = 'miniblog'
    
    def ready(self):
        import miniblog.signals
