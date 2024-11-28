from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserRegistration
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from .models import Complaint
from .models import Feedback

class CustomLoginForm(AuthenticationForm):
    username = None  # Remove the default username field
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
        label="Email",
        required=True
    )


class UserRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    class Meta:
        model = UserRegistration
        fields = ['full_name', 'email', 'contact_number', 'password', 'confirm_password', 'emergency_contact1', 'emergency_contact2']
        widgets = {
            'password': forms.PasswordInput,
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password != confirm_password:
            raise ValidationError("Passwords do not match.")
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'phone', 'location', 'incident_type', 'incident_date', 'complaint']
        widgets = {
            'incident_date': forms.DateInput(attrs={'type': 'date'}),
            'complaint': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'feedback', 'rating', 'suggestion']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email'}),
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write your feedback'}),
            'rating': forms.Select(attrs={'class': 'form-select'}),
            'suggestion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Any suggestions?'}),
        }
