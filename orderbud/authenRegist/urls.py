from django.contrib import admin
from django.urls import path
from django.urls import include
from authenRegist.views import login_view
urlpatterns = [
    path('', login_view, name = "login_view")
]