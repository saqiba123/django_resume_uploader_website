from django import forms
from django.forms import fields, widgets
#from django.forms.models import Labels
from .models import Resume

# make choices for gender in key value form
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
]

JOB_CITY_CHOICE = [
    ('Karachi', 'Karachi'),
    ('Islamabad', 'Islamabad'),
    ('Lahore', 'Lahore'),
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(
        label='Preferred Job Locations', choices=JOB_CITY_CHOICE, widget=forms.CheckboxSelectMultiple)
    # write class meta

    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender',
                  'city', 'pin', 'state', 'mobile', 'email', 'job_city', 'profile_image', 'my_file']
        labels = {'name': 'Full Name', 'dob': 'Date of Birth',
                  'pin': 'Pin Code', 'mobile': 'Mobile No', 'email': 'Email ID',
                  'profile_image': 'Profile Image', 'my_file': 'Document'}
        # we have to add css for fields from bootstrtap using widgets
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
