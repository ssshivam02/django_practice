from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
# we using templateview directly in urls.py

# Create your views here.

class ShivamSharmaRedirectView(RedirectView):
    url = 'https://www.google.com'
    
    
class ShivamRedirectView(RedirectView):
    # url = '/'
    pattern_name = 'mindex'
    permanent = True  #301 redirection
    # permanent = False #302 redirection by default
    # query_string = False # this will not allow query in url by default.
    query_string = True # we will get query string in url
    
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        print(kwargs) # we get key values. {'pk':36}
        kwargs['pk']=16 #default value
        return super().get_redirect_url(*args, **kwargs)
    