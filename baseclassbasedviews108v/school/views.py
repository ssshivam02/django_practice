from django.shortcuts import render
from django.http import HttpResponse
# class Based view
from django.views import View
from school.forms import ContactForm
# Create your views here.
# function based view
def myview(request):
    # by default get is working here
    return HttpResponse('<h1>Function Based View</h1>')

# template view
def homefun(request):
    return  render(request, 'school/home.html',{'view':'Function'})

# forms
def contactfun(request):
    if request.method == 'POST':
        print(request.method)
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you Form Submitted')
    else:
        form = ContactForm()
        return  render(request, 'school/contact.html',{'form':form})

def newsfun(request):
    template_name = 'school/news.html'
    context = {'info': 'CBI Enquiry'}
    return render(request, template_name,context)

def newsfun_parameter(request, template_name):
    context = {'info': 'CBI Enquiry'}
    return render(request, template_name,context)

# Class Based View
class MyView(View):
    name = 'Prapti'
    def get(self, request):
        # return HttpResponse('<h1>Class Based View</h1>')
        return HttpResponse(self.name)
    
# child class    
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)

# class based view template   
class HomeClassView(View):
    def get(self, request):
        return render(request, 'school/home.html', {'view':'Class'})
    
class ContantClassView(View):
    def get(self, request):
        form = ContactForm()
        return  render(request, 'school/contact.html',{'form':form})
    
    def post(self, request):
        print(request.method)
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank you Form Submitted')
        
        
class NewsClassView(View):
    def get(self, request):
        template_name = 'school/news.html'
        context = {'info': 'CBI Enquiry'}
        return render(request, template_name, context)
    
class NewsClassViewParameter(View):
    def get(self, request, template_name):
        context = {'info': 'CBI Enquiry'}
        return render(request, template_name, context)
