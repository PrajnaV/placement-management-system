from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
import datetime

class StudentProfile(models.Model):
    branch_choices = (
        ('IT', 'Information technology'),
        ('ME', 'Mechanical'),
        ('CV', 'Civil'),
        ('EEE', 'Electronics and Electrical'),
        ('ECE', 'Electronics and Communication'),
        ('CH', 'Chemical'),
        ('CSE', 'Computer Science'),
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
    degree = models.CharField(blank=True,choices=degree_options)
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

class JobPost(models.Model):
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    designation = models.CharField(max_length=30, blank=False)
    salary = models.IntegerField(blank=False)
    bond_years = models.IntegerField(blank=False)
    created_at = models.DateField(auto_now_add=True)
    requirement = models.TextField(blank=True)
    closing_date = models.DateField(blank=True, default=datetime.date(2024, 12, 31))

    def __str__(self):
        return f"{self.designation} - {self.company.user.username}"
    
class AppliedJob(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    ]
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')