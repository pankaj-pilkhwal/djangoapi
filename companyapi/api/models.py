from django.db import models

# Company Model
class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100,
                             choices=(("IT", "IT"),
                                      ("Non-IT", "Non-IT"),
                                      ("Agriculture", "Agriculture"),
                                      ("Pharma", "Pharma")
                                      ))
    added_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField(max_length = 200)
    position= models.CharField(max_length=50, 
                               choices=(('Manager', 'Manager'),
                                        ('Software Developer', 'Software Developer'),
                                        ('Project Leader', 'Project Leader')
                                        ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
