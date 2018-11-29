from django.shortcuts import render
from django.http import HttpResponse
from ex_app.models import Company, Department, Employees
from . import forms

# Create your views here.
def index(request):
    # return HttpResponse("hello i am index in views !!")
    # index_dict = {'insert_index_from_views':'hello i am from index in views !!'}
    # return render(request, 'ex_app/index.html', context=index_dict)
    Employees_Rows = Employees.objects.order_by('Emp_FName')
    # Employees_dic = {'Employees_Rows': Employees_Rows}
    form = forms.FormAddCompany()
    return render(request, 'ex_app/index.html', context={'Employees_Rows':Employees_Rows,'form':form})


def about(request):
    # return HttpResponse("hello i am about in views !!")
    about_dict = {'insert_about_from_views': 'hello i am from about in views !!'}
    return render(request, 'ex_app/about.html', context=about_dict)

# def form_add_comp(request):
#     form = forms.FormAddCompany()
#     return render(request, 'ex_app/index.html', {'form':form})