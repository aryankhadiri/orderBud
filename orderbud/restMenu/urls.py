from django.contrib import admin
from django.urls import path
from django.urls import include
from landing.views import food_view

urlpatterns = [
    path('', food_view, name = "food_page"),
]
