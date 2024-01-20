from django.test import TestCase
from django.urls import reverse
from django.core import exceptions
from django.db import IntegrityError
from employees import models


class EmployeeListTestCase(TestCase):

    def test_get_status_and_template(self):
        response = self.client.get(reverse("employee:employee-get-list"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,"employee_get_list.html")
    
    def test_invalid_employee_cred(self):
        response = self.client.post(reverse("employee:employee-get-list"),{"email":"notfound@abc.com"})
        self.assertEqual(response.status_code,404)
        self.assertIn("Invalid Credentials..",str(response.content))
    

class EmployeeModelsTestCase(TestCase):

    def setUp(self) -> None:
        self.holiday_obj = models.HolidayCategory.objects.create(name="demo category")
        self.emp_obj = models.Employee.objects.create(first_name="Demo",last_name="Demo",
                                       email="demo@abc.com")
        self.emp_obj.holiday_category.add(self.holiday_obj)
        models.Holiday.objects.create(name="demo",date="2024-01-01",holiday_category=self.holiday_obj)
    
    def test_holiday_category_is_none(self):
        with self.assertRaises(exceptions.ObjectDoesNotExist):
            models.HolidayCategory.objects.get(name="not found")

    def test_holiday_category_read(self):
        loc_obj = models.HolidayCategory.objects.get(name="demo category")
        self.assertEqual(loc_obj.name,"demo category")

    def test_employee_is_none(self):
        with self.assertRaises(exceptions.ObjectDoesNotExist):
            models.Employee.objects.get(email="not found") 

    def test_employee_read(self):
        emp_obj = models.Employee.objects.get(email="demo@abc.com")
        self.assertEqual(emp_obj.email,"demo@abc.com")
    
    def test_employee_email_unique(self):
        with self.assertRaises(IntegrityError):
            models.Employee.objects.create(first_name="Demo",last_name="Demo",
                                        email="demo@abc.com")
    
    def test_holiday_is_none(self):
        with self.assertRaises(exceptions.ObjectDoesNotExist):
            models.Holiday.objects.get(name="not found")        

    def test_holiday_read(self):
        holiday_obj = models.Holiday.objects.get(name="demo")
        self.assertEqual(holiday_obj.name,"demo")