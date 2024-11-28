from django.shortcuts import render, HttpResponse, redirect
from auth_app.models import Story
from auth_app.models import UserRegistration
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from auth_app.forms import UserRegistrationForm
from django.contrib.auth import login, logout #type: ignore
from .middlewares import auth, guest
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm
from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .forms import ComplaintForm
from .forms import FeedbackForm

# Create your views here.
def home_view(request):
     return render(request, 'home.html')

@guest
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in or redirect
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'auth/register.html', {'form': form})

@guest
def login_view(request):
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')  # Fetch the email from the form
        password = request.POST.get('password')  # Fetch the password from the form
        
        try:
            # Check if a user with the provided email exists
            user = UserRegistration.objects.get(email=email)
            
            # Verify the password
            if check_password(password, user.password):
                # Create a session for the user
                request.session['user_id'] = user.id
                request.session['user_email'] = user.email  # Optional: Store more session data if needed
                return render(request, 'dashboard.html')
            else:
                error_message = "Invalid email or password."
        except UserRegistration.DoesNotExist:
            error_message = "Invalid email or password."
    
    # Render the login page with an error message if login fails
    return render(request, 'auth/login.html', {'error_message': error_message})

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def submit_complaint(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your complaint has been submitted successfully.")
            return redirect('complaint')
    else:
        form = ComplaintForm()
    
    return render(request, 'complaint_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render

def story_view(request):
    return render(request, 'story.html')

def submit_story(request):
    if request.method == 'POST':
        content = request.POST.get('story_content', '')
        if content:
            Story.objects.create(content=content)
            messages.success(request, 'Your story has been submitted successfully!')
            return redirect('story_view')  # Redirect back to the same page
    messages.error(request, 'Failed to submit your story. Please try again.')
    return redirect('story_view')
    
def story_feed(request):
    stories = Story.objects.all()
    return render(request, 'story_feed.html', {'stories': stories})

def self_defense(request):
    return render(request, 'self_defense.html')

def mensus(request):
    return render(request, 'mensus.html')

def gynec(request):
    return render(request, 'gynec.html')

def laws(request):
    return render(request, 'laws.html')

def memorialwall_view(request):
     return render(request, 'memorialwall.html')

def Ngo(request):
    return render(request, 'Ngo.html')

def location(request):
    return render(request, 'location.html')

def feedback(request):
    return render(request, 'feedback.html')

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your complaint has been submitted successfully.")
            return redirect('feedback') 
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

    

class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'