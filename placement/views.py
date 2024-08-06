from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import auth
from .forms import UserForm, StudentProfileForm, CompanyProfileForm, CreateJobForm
from django.contrib.auth.decorators import login_required

from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login_user')     
def logout(request):
    auth.logout(request)
    return redirect('/')

def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)   #checks if the user already registered in database

        if user is not None:    #if user exists
            auth.login(request,user)
            if StudentProfile.objects.filter(user=user).exists():
             return redirect('student_dashboard')
            elif CompanyProfile.objects.filter(user=user).exists():
             return redirect('company_dashboard')
            else:
             return redirect('index')  # Default redirection if user type is not identified
            
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login_user')
    else:
        return render(request,'login.html')
    
def stu_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = StudentProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user.email
            profile.save()
            login(request, user)
            return redirect('student_dashboard') #here I have assumed that username is unique for each user
    else:
        user_form = UserForm()
        profile_form = StudentProfileForm()
    return render(request, 'studentregister.html', {'user_form': user_form, 'profile_form': profile_form})
    

def comp_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = CompanyProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.email = user.email
            profile.save()
            login(request, user)
            return redirect('company_dashboard')
    else:
        user_form = UserForm()
        profile_form = CompanyProfileForm()
    return render(request, 'companyregister.html', {'user_form': user_form, 'profile_form': profile_form})
    
@login_required(login_url='login_user')
def student_dashboard(request):
    return render(request,'studentdashboard.html')

@login_required(login_url='login_user')
def student_profile_view(request):
    user_object = request.user 
    user_profile = StudentProfile.objects.get(user=user_object)
    return render(request,'studentprofile.html',{'user_profile':user_profile})

@login_required(login_url='login_user')
def update_studentprofile(request):
    user_object = request.user 
    current_record = StudentProfile.objects.get(user=user_object)
    form = StudentProfileForm(request.POST or None, instance=current_record)  #uses addrecordform to update where the fields of the form will be 
                                                                          #already filled with current instance values
    if form.is_valid():
        form.save()
        messages.success(request, "Updated successfully !")
        return redirect('update_studentprofile')
    return render(request,'update.html',{'form':form})

@login_required(login_url='login_user')
def create_job(request):
    if request.method == 'POST':
        form = CreateJobForm(request.POST)
        if form.is_valid():
            job_post = form.save(commit=False)
            job_post.company = CompanyProfile.objects.get(user=request.user)
            job_post.save()
            return redirect('company_dashboard')  # Redirect to some view after successful submission
    else:
        form = CreateJobForm()
    return render(request,'createjob.html',{'form':form})

@login_required(login_url='login_user')
def company_dashboard(request):
    return render(request,'companydashboard.html')