from typing import Any
from django import forms
from django.contrib import admin
from employees import models


@admin.register(models.Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]

    class Meta:
        verbose_name_plural = "Location"

@admin.register(models.Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["email","location"]
    list_filter = ["location",]


class HolidayForm(forms.ModelForm):
    def clean(self) -> None:
        holiday_type = self.cleaned_data["holiday_type"]
        location = self.cleaned_data["location"]
        if holiday_type == "local" and not location:
            raise forms.ValidationError("Location must be selected for holiday type local")
        return self.cleaned_data

@admin.register(models.Holiday)
class HolidayAdmin(admin.ModelAdmin):
    form = HolidayForm
    list_display = ["name","date","holiday_type","location"]
    list_filter = ["holiday_type","location"]

    class Meta:
        verbose_name_plural = "Holiday"