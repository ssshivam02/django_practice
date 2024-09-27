from django.shortcuts import render
from school.models import Student

# Create your views here.
def all_student(request):
    # Retrieving all objects
    student_data= Student.objects.all() #returns queryset 
    print("SQL Query:", student_data.query)
    return render(request,'school/home.html', {'students': student_data})

#Retrieving Specific object
def one_student(request):
    student_data = Student.objects.filter(address='patna')
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html', {'students':student_data})
    
  
# exclude  
def exclude_student(request):
    student_data = Student.objects.exclude(marks=93)
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html', {'students':student_data})

#order_by(*fields) - It orders the field.
#'field' -Asc order.
#-field -Desc order.
# '?'- Randomly.
def order_by_student(request):
    # student_data = Student.objects.order_by('-marks') # for desc
    # student_data = Student.objects.order_by('marks') # for asc
    student_data = Student.objects.order_by('?') # for randomly # order is dome by unicode.
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html', {'students':student_data})

# reverse() - This work only when there is ordring in queryset.
def reverse_student(request):
    # student_data = Student.objects.order_by('marks').reverse() # reverse the order of the queryset
    student_data = Student.objects.order_by('marks').reverse()[:1] # only 1, first 1
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html', {'students':student_data})

# values() - It returns a QuerySet that returns dictionaries, rather than model instances, when used as an iterable. Each of those dictionaries represents an object, with the keys corresponding to the attribute names of model objects.
def values(request):
    # student_data = Student.objects.values() # this will return dictionary
    student_data = Student.objects.values('name', 'address') # only name and address will get.
    print('SQL query:', student_data.query)
    for student in student_data:
        print(student) #
    return render(request, 'school/home.html',{'students':student_data})

#distinct(*fields) - This eleiminates duplicate rows from the query results.
def distinct(request):
    student_data = Student.objects.values('marks').distinct() # only marks will get.
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html',{'students':student_data})

#values_list(*fields, flat= False, named=False)
def values_list(request):
    # student_data = Student.objects.values_list('name', 'address') # returns tuple
    student_data = Student.objects.values_list('name', 'address', named= True) # returns tuple with attribute    
    print('SQL Query:', student_data.query)
    for student in student_data:
        print(student) #
    return render(request,'school/home.html',{'students':student_data})

#using(alias) - This method is for controlling which database the QuerySet will be evaluated against if you are using more than one database. The only arugment this method takes is the alias of a database, as defined in DATABASES.
# EXAMPLE:- student_data = Student.objects.using('default')
def using_alias(request):
    student_data = Student.objects.using('default') # name of database
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html',{'students':student_data})

#dates(field, kind, order='ASC) - It returns a QuerySet that evaluates to a list of a list of datetime.date objects
# representing all available dates of a particular kind within the contents of the QuerySet.
# where, field - It should be the name of a DteField of your model.
# kind- It should be either "year", "month","week" or "day".
# "year" returns a list of all distinct year values for the field.
# "month" returns a list of all distinct yearANDmonth values for the field.
# "week" returns a list of all distinct year/week values for the field. All dates will be a Monday.
# "day" return a list of all distinct year/month/day values for the field.
# order - It should be either "ASC" or "DESC". defaults to 'ASC'.
def dates(request):
    student_data = Student.objects.dates('pass_date', 'month', order='ASC') # pass_date
    print('SQL Query:', student_data.query)
    return render(request,'school/home.html',{'students':student_data})

# datetimes(field_name, kind, ordr='ASC' tzinfo=None) tzinfo timezone info

#none() - EmptyQuerySet()
#union(*other_qs, all=False) #to allow duplicate values, use the all = True argument.
# Uses SQL's UNION operator to combine the results of two or more QuerySets. The UNION operator selects only distinct values by default.
# student_data = qs2.union(qs1, all=True) all data

#intersection(*other_qs)- Uses SQL's  Intersect operator to return the shared elements of two or more QuerySets.
# Eample:- student_data = qs1.intersection(qs2)

# Operators that return new QuerySets
# ----------------------------------------
# AND(&) Combines two QuerySets using the SQL AND operator.
#example:- student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=93)
    # Student.objects.filter(id=6, roll=93)
    # student_Data = Student.objects.filter(Q(id=6) & Q(roll=106))
    
# OR(|) Combines two QuerySets using the SQL OR operator.
# example:- student_data = Student.objects.filter(id=6) | Student.objects.filter(roll=
# 93)
# student_data = Student.objects.filter(Q(id=6) | Q(roll=93))
# NOT(~) Negates a QuerySet.
# example:- student_data = ~Student.objects.filter(id=6)
# student_data = ~Student.objects.filter(Q(id=6))
# Q() - It is used to build a complex lookup by combining filters with the AND, OR
# operators. It is used to build a complex lookup by combining filters with the AND, OR operators
# example:- student_data = Student.objects.filter(Q(id=6) & Q(roll=93
# student_data = Student.objects.filter(Q(id=6) | Q(roll=93)
# for Q object
from django.db.models import Q
