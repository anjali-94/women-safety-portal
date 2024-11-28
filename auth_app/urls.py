from django.urls import path #type:ignore
from . import views
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from .views import submit_complaint

urlpatterns=[
    path('', views.home_view, name='home'),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('dashboard/', views.dashboard_view,name='dashboard'),
    path('logout/', views.logout_view,name='logout'),
    path('story/', views.story_view, name='story'),
    path('story/submit/', views.submit_story, name='submit_story'),
    path('story/', views.story_view, name='story'),
    path('story/view/', views.story_view, name='story_view'),
    path('story-feed/', views.story_feed, name='story_feed'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('memorialwall/', views.memorialwall_view, name='memorialwall'),
    path('complaint/', views.submit_complaint, name='complaint'),
    path('self_defense/', views.self_defense, name='self_defense'),
    path('mensus/', views.mensus, name='mensus'),
    path('gynec/', views.gynec, name='gynec'),
    path('laws/', views.laws, name='laws'),
    path('Ngo/', views.Ngo, name='Ngo'),
    path('location/',views.location,name='location'),
    path('feedback/view/', views.feedback, name='feedback_view'),
    path('feedback/', views.feedback_view, name='feedback'),
   
]