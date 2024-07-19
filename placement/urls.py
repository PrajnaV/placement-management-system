from django.urls import path
from . import views
from .views import CustomLoginView

urlpatterns = [
    path('',views.index,name='index'),
    path('logout/',views.logout,name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('stu_register/',views.stu_register,name='stu_register'),
    path('comp_register/',views.comp_register,name='comp_register'),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('company_dashboard/', views.company_dashboard, name='company_dashboard'),
]