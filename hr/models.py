from django.db import models


# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.name, self.location)

    class Meta:
        db_table = 'departments'


class Employee(models.Model):
    name = models.CharField(max_length=30)
    job = models.CharField(max_length=50)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete='cascade')

    def __str__(self):
        return "%s,%s,%d" % (self.name, self.job, self.salary)

    class Meta:
        db_table = 'Employees'  # Name to be used in database
