from django.urls import path
from employees import views

#namespace
app_name = "employee"

urlpatterns = [
    path('', views.employee_get_list,name="employee-get-list"),
]
