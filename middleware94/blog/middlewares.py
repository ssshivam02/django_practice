# get_response arugment is nessary.
from django.shortcuts import HttpResponse
def my_middleware(get_response):
    print("One Time initialization") # when we start server
    def my_function(request):
        print("This is before view")
        response = get_response(request)
        print("This is after view")
        return response
    return my_function

# class based Middleware
class SonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Son initialization-class") # when we start server
    def __call__(self, request):
        print("This is Son before view- class")
        response = self.get_response(request)
        print("This is Son after view-class")
        return response

class FatherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Father initialization-class") # when we start server
    def __call__(self, request):
        print("This is Father before view- class")
        response = self.get_response(request)
        # for stopping her middleware, dont go to MotherMiddleware
        # response= HttpResponse("Nikl lo") #this will not go to views and next middleware
        print("This is Father after view-class")
        return response
    
class MotherMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("One Time Mother initialization-class") # when we start server
    def __call__(self, request):
        print("This is Mother before view- class")
        response = self.get_response(request)
        print("This is Mother after view-class")
        return response
