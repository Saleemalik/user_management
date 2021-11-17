from django.urls import path
from .views import *

urlpatterns = [
    path('', userLogin, name='login'),
    path('signup', userSignup, name='signup'),
    path('userpage', userPage, name='userpage'),
    path('userpage/<int:id>', deleteUser, name='userpage'),
    path('edit/<int:id>', editUser, name='editUser'),
    path('logout', logout, name='logout'),
    
]   