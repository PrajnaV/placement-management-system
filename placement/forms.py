from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import StudentProfile, CompanyProfile

class UserForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class StudentProfileForm(forms.ModelForm):
    phone_number = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
    cgpa = forms.FloatField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"CGPA", "class":"form-control"}), label="")
    skills = forms.CharField(required=False,widget=forms.Textarea(attrs={
            "placeholder": "Enter your skills separated by commas",
            "class": "form-control",
            "rows": 3
        }),
        label=""
    )
    bio = forms.CharField(required=False,widget=forms.Textarea(attrs={
            "placeholder": "Bio",
            "class": "form-control",
            "rows": 3
        }),
        label=""
    )
    
    class Meta:
        model = StudentProfile
        fields = ( 'phone_number','branch','gender','cgpa','skills','bio','profileimg')

    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        
        # Customize the label and attributes for a specific field
        self.fields['branch'].label = 'Branch'
        self.fields['branch'].widget.attrs.update({'class': 'form-select'})
        self.fields['branch'].label_tag = '<label  class="form-label">%s</label>' % ( self.fields['branch'].label)

        self.fields['gender'].label = 'Gender'
        self.fields['gender'].widget.attrs.update({'class': 'form-select'})
        self.fields['gender'].label_tag = '<label  class="form-label">%s</label>' % ( self.fields['gender'].label)
    
   
class CompanyProfileForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ( 'hr_name', 'hr_phn', 'headquarters')
