from django.db import models

# Company Model
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                             choices=(("IT","IT"),
                                      ("Non-IT","Non-IT"),
                                      ("Agriculture","Agriculture")
                                      ))
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

# Employee Model
class Employee(models.Model):
    pass