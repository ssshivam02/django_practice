from django.shortcuts import HttpResponse

class MyProcessMiddleware:
    def __init__(self, get_response):
        print("This is hook initialization")
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_view(request, *args, **kwargs):
        print("This is process view - Before view")
        return None
        # return HttpResponse("This is before view")
        


class MyExceptionMiddleware:
    def __init__(self, get_response):
        print("This is Exception hook initialization")
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):
        print("exception occured")
        msg = exception
        class_name = exception.__class__.__name__
        print(class_name)
        print(32,msg)
        return HttpResponse(msg)
    
class MyTemplateResponseMiddleware:
    def __init__(self, get_response):
        print("This is MyTemplateResponseMiddleware hook initialization")
        self.get_response = get_response
        
    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def process_template_response(self, request, response):
        print("Process Template Response from middleware")
        response.context_data['name'] = 'shivam' #it will update
        return response