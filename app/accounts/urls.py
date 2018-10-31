from django.urls import path
from django.contrib.auth.views import auth_login

from . import views

urlpatterns = [
    # path('login/', auth_login, name='login', kwargs={
    #     'template_name': 'accounts/login.html'
    # })
    path('login/', views.login, name='login'),
]
