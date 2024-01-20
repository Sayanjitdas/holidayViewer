from typing import Any
from django import forms
from django.contrib import admin
from employees import models


@admin.register(models.HolidayCategory)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]


@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["email","holiday_categories"]

    def holiday_categories(self,obj):
        categories = obj.holiday_category.all()
        print(list(categories))
        return [category for category in list(categories)]

@admin.register(models.Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = ["name","date","holiday_category"]
