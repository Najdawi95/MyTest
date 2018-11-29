from django.db import models


# Create your models here.
class Company(models.Model):
    Comp_Name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.Comp_Name


class Department(models.Model):
    Comp_Name = models.ForeignKey(Company, on_delete=models.CASCADE, )
    Dept_Name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.Dept_Name


class Employees(models.Model):
    Emp_FName = models.CharField(max_length=255)
    Emp_LName = models.CharField(max_length=255)
    Emp_Email = models.TextField(max_length=50)
    Emp_Phone = models.IntegerField(max_length=50)
    Comp_Name = models.ForeignKey(Company, on_delete=models.CASCADE, )
    Dept_Name = models.ForeignKey(Department, on_delete=models.CASCADE, )

    def __str__(self):
        return self.Emp_FName + " " + self.Emp_LName
