from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=10)
    branch = models.CharField(max_length=100)
    cgpa = models.FloatField()

    def __str__(self):
        return self.user.username
    

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hr_name = models.CharField(max_length=30)
    hr_phn = models.CharField(max_length=10)
    headquarters = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
