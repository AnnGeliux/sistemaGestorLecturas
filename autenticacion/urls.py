
from django.urls import path
from .views import CustomLoginView, register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', register, name='register'),
]
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
