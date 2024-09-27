from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.

class HomeTemplateView(TemplateView):
    template_name = 'school/home.html'
    

# context use
class HomeTemplateContextView(TemplateView):
    print("HELLO")
    template_name = 'school/home.html'
    def get_context_data(self, **kwargs):
        # (extra_context={"course":"Python"}
        # kwargs content path parameter.
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home Page'  
        context['roll'] = 101
        print(context)
        return context