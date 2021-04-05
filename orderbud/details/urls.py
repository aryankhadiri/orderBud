from django.urls import path
from django.urls import include
from .views import restaurants_details_view

urlpatterns = [
    path("restaurants/<int:id>", restaurants_details_view, name = "rest_view")
]