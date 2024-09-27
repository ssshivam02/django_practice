from django.shortcuts import render
from django.views.generic.list import ListView
from school.models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student    # all student details in model
    template_name = 'school/student.html' # this will also work # custom template is more priority
    # custom file name
    # template_name_suffix = '_list' #by default
    # template_name_suffix = '_get'
    ordering = ['name']
    
    # custom context name
    context_object_name = 'students'
    # by using above code we get this
    # stud = Student.objects.all()
    # context = {'student_list':stud}
    # return render(request, 'school/student_list.html', context)
    def get_queryset(self):
        return Student.objects.filter(course = 'python')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fresher"] = Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self):
        if self.request.COOKIES['user']=='sonam':
            return [""]
        return super().get_template_names()
    