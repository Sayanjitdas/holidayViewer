from django.shortcuts import render
from employees import models,forms
from django.db.models import Q

def employee_holiday_list(request):
    data = {}
    status = 200
    if request.method == "POST":
        emp_form = forms.EmployeeListForm(request.POST)
        if emp_form.is_valid():
            emp_email = request.POST.get("email")
            emp_obj = models.Employee.objects.get(email=emp_email)
            categories = emp_obj.holiday_category.all()
            holidays = models.Holiday.objects.filter(holiday_category__in=categories)
            data["holidays"] = holidays
            return render(request,"list_holiday.html",data)
        else:
            value = emp_form.errors.as_data().get("email")
            data["error"] = value[0].message
            status = value[0].code       
    
    return render(request,"employee_get_list.html",data,status=status)
    
