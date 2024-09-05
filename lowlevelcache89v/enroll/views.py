from django.shortcuts import render
from django.core.cache import cache
# Create your views here.
# def home(request):
#     # mv = cache.get('movie', 'has_expired')
#     # if mv=='has_expired':
#     #     cache.set(
#     #         'movie','The manjhi', 30
#     #     )
#     #     mv = cache.get('movie')
#     fee = cache.get_or_set('fees',3000,30, version =2)
#     return render(request, 'enroll/course.html', {'mv':fee})

# def home(request):
#     data ={'name':'sonam', 'roll':101}
#     cache.set_many(data,30)
#     sv = cache.get_many(data)
#     print(sv)
#     return render(request, 'enroll/course.html',{'fm':sv})

# def home(request):
#     cache.delete('fees', version =2)
#     return render(request, 'enroll/course.html')

# def home(request):
#     # cache.set('roll', 101,600)
#     # rv= cache.get('roll')
#     dv=cache.decr('roll', delta=1)
#     print(dv)
#     return render(request, 'enroll/course.html',)

def home(request):
    cache.clear()
    return render(request,'enroll/course.html')
