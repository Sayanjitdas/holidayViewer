from django.db import models


class Location(models.Model):
    """The model used to save different location 
    of the residing employees based on which holiday will
    be filtered
    """
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Location"

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    """This is the employee model
    """
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255,blank=True,default="")
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    employee_id = models.CharField(max_length=255,unique=True,blank=True,null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Employee"

    def __str__(self) -> str:
        return self.email


class Holiday(models.Model):
    """The holiday list model
    """
    class HolidayType(models.TextChoices):
        national = "national", "national"
        local = "local", "local"

    name = models.CharField(max_length=255)
    date = models.DateField()
    holiday_type = models.CharField(max_length=20,
                                    choices=HolidayType.choices,default=HolidayType.national)
    location = models.ForeignKey(Location,on_delete=models.DO_NOTHING,null=True,blank=True)

    class Meta:
        verbose_name_plural = "Holiday"

    def __str__(self) -> str:
        return self.name