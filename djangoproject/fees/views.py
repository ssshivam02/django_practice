from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def fees_django(request):
    d = datetime.now()
    return render(request, 'fee/feesone.html', {'dt' : d})

def fees_python(request):
    
    return render(request, 'fee/feestwo.html',{
        'p1':56.2321,
        'p2':56.0000,
        'p3':56.3700        
    })