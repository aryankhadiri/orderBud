from django.contrib import admin
from django.urls import path
from .views import landing_view, search_result_view

urlpatterns = [
    path('', landing_view, name = "landing_view"),
    path('searchresult/', search_result_view, name = "search_result_view")
]