from django.contrib import admin
from ex_app.models import Company, Department, Employees

# Register your models here.
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Employees)