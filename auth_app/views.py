from django.shortcuts import render, redirect # type: ignore
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth import login, logout #type: ignore
from .middlewares import auth, guest
from .models import Story
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

# Create your views here.

def home_view(request):
     return render(request, 'home.html')


@guest
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'', 'password1':'', 'password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})
@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user= form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'', 'password1':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form})

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import render

def story_view(request):
    stories = Story.objects.all()
    return render(request, 'story.html', {'stories': stories})

def submit_story(request):
    if request.method == 'POST':
        content = request.POST.get('story_content', '')
        if content:
            Story.objects.create(content=content)
    return redirect('story')


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'login.html'