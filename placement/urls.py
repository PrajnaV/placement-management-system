from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('login_user/', views.login_user, name='login_user'),
    path('stu_register/',views.stu_register,name='stu_register'),
    path('comp_register/',views.comp_register,name='comp_register'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('company_dashboard/', views.company_dashboard, name='company_dashboard'),
    path('student_profile_view/', views.student_profile_view, name='student_profile_view'),
    path('update_studentprofile/', views.update_studentprofile, name='update_studentprofile'),
    path('create_job/', views.create_job, name='create_job'),
    path('applyjob/', views.applyjob, name='applyjob'),
    path('view_applicants/<int:job_id>/', views.view_applicants, name='view_applicants'),
    path('application_status/', views.application_status, name='application_status'),

]