from django.shortcuts import render

# Create your views here.
# dynamic template
def learn_django(request):
    coursename = {'cname' : 'Django is awesome'}
    return render(request, 'course/courseone.html', context = coursename)

def if_tag_example(request):
    return render(request, 'course/iftagexample.html', {'nm': False})

def learn_python(request):
    cname = 'Python'
    duration = '4 Months'
    seats = 10
    python_details = {'nm': cname, 'du': duration, 'st': seats}
    return render(request, 'course/coursetwo.html', python_details )


def for_loop_example(request):
    student = {'names': ['Shivam', 'Rahul', 'Pratik', 'Prapti']}
    # student = {'names': []}
    return render(request, 'course/forloopexample.html', student)


def for_dict_example(request):
    stu = {
        'stu1': {'name': 'Rahul', 'roll': 101},
        'stu2': {'name': 'Shivam', 'roll': 102},
        'stu3': {'name': 'Krish', 'roll': 103},
        'stu4': {'name': 'Suraj', 'roll': 104},
    }
    student = {'students': stu}
    return render(request, 'course/for_dict.html', student)