from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    branch_choices = (
        ('it', 'Information technology'),
        ('me', 'Mechanical'),
        ('cv', 'Civil'),
        ('eee', 'Electronics and Electrical'),
        ('ece', 'Electronics and Communication'),
        ('ch', 'Chemical'),
        ('cse', 'Computer Science'),
    )
    gender = (
        ('male', 'male'),
        ('female', 'female'),
        ('others','others'))
    degree_options = (
        ('btech','B.Tech'),
        ('mtech','M.Tech'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    branch = models.CharField(blank=False, choices=branch_choices)
    gender=models.CharField(blank=False, choices=gender,max_length=10)
    cgpa = models.FloatField()
    degree = models.CharField(blank=False,choices=degree_options)
    skills = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='images',default='blank_user.png')

    def __str__(self):
        return self.user.username
    

class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hr_name = models.CharField(max_length=30)
    hr_phn = models.CharField(max_length=10)
    headquarters = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username
