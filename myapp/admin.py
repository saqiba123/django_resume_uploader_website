from django.contrib import admin
from .models import Resume

# Register your models here.

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'dob', 'gender',
    'city', 'pin','state', 'mobile','email','job_city','profile_image','my_file']

