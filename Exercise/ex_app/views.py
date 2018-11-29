from django.shortcuts import render
from django.http import HttpResponse
from ex_app.models import Company, Department, Employees


# Create your views here.
def index(request):
    # return HttpResponse("hello i am index in views !!")
    # index_dict = {'insert_index_from_views':'hello i am from index in views !!'}
    # return render(request, 'ex_app/index.html', context=index_dict)
    Employees_Rows = Employees.objects.order_by('Emp_FName')
    Employees_dic = {'Employees_Rows': Employees_Rows}
    return render(request, 'ex_app/index.html', context=Employees_dic)


def about(request):
    # return HttpResponse("hello i am about in views !!")
    about_dict = {'insert_about_from_views': 'hello i am from about in views !!'}
    return render(request, 'ex_app/about.html', context=about_dict)
