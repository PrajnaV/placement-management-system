from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.contrib.auth.models import auth
from .forms import UserForm, StudentProfileForm, CompanyProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')     
def logout(request):
    auth.logout(request)
    return redirect('/')

def stu_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = StudentProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = StudentProfileForm()
    return render(request, 'studentregister.html', {'user_form': user_form, 'profile_form': profile_form})
    

def comp_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = CompanyProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('index')
    else:
        user_form = UserForm()
        profile_form = CompanyProfileForm()
    return render(request, 'companyregister.html', {'user_form': user_form, 'profile_form': profile_form})
    

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        user = self.request.user
        if StudentProfile.objects.filter(user=user).exists():
            return reverse_lazy('index')
        elif CompanyProfile.objects.filter(user=user).exists():
            return reverse_lazy('index')
        else:
            return reverse_lazy('index')  # Default redirection if user type is not identified
        
def student_dashboard(request):
    return render(request,'studentdashboard.html')

def company_dashboard(request):
    return render(request,'companydashboard.html')