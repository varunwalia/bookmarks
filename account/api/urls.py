from django.urls import path,include
from django.contrib import admin

from . import views


app_name = 'account'

urlpatterns = [
	path('users/',views.UserListView.as_view() , name='users'),
    # path('login/', views.UserLoginAPIView.as_view(), name='login'),
    # path('register/', views.UserCreateAPIView.as_view(), name='register'),
]
