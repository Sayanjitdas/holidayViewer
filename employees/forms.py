from django import forms
from django.core import exceptions
from employees import models

class EmployeeListForm(forms.Form):
    email = forms.CharField(max_length=255)
    
    def clean_email(self):
        emp_email = self.cleaned_data.get("email")
        try:
            _ = models.Employee.objects.get(email=emp_email)
        except exceptions.ObjectDoesNotExist:
            raise forms.ValidationError("Invalid Credentials..",code=404)