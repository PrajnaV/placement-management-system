from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(StudentProfile)
admin.site.register(CompanyProfile)
admin.site.register(JobPost)
admin.site.register(AppliedJob)