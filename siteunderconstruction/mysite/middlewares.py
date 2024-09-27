from django.shortcuts import render
class UnderConstructionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        print("call from Middleware")
        response = render(request, "mysite/uncont.html")
        print("Call from Middleware after view")
        return response 