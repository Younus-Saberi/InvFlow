from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
]