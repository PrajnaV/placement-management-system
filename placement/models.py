from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator

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
    email = models.EmailField(max_length=200,null=True)
    phone_number = models.CharField(max_length=10)
    branch = models.CharField(blank=True, choices=branch_choices)
    gender=models.CharField(blank=True, choices=gender,max_length=10)
    cgpa = models.FloatField(validators=[MinValueValidator(0),MaxValueValidator(10)],blank=False,help_text='*required')
    
    skills = models.TextField(blank=True)
    bio = models.TextField(blank=True)
    profileimg = models.ImageField(upload_to='student',default='blank_user.png')

    def __str__(self):
        return self.user.username
    

class CompanyProfile(models.Model):
    type_choices =(
        ('service','service based'),
        ('product','product based')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=200,null=True)
    hr_name = models.CharField(max_length=30)
    hr_phn = models.CharField(max_length=10)
    headquarters = models.CharField(max_length=30)
    type_of_company = models.CharField(blank=True,choices=type_choices) 
    desc = models.TextField(blank=True)
    logo = models.ImageField(upload_to='company',default='blank_user.png')

    def __str__(self):
        return self.user.username
