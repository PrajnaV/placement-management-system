from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('login_user/', views.login_user, name='login_user'),
    path('stu_register/',views.stu_register,name='stu_register'),
    path('comp_register/',views.comp_register,name='comp_register'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('company_dashboard/', views.company_dashboard, name='company_dashboard')
]