from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from user import views
from user.views import *


app_name = 'user'


urlpatterns = [
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
]
