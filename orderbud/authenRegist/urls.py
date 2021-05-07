from django.contrib import admin
from django.urls import path
from django.urls import include
from authenRegist.views import login_view, register_view, logout_view, messages_view, send_message_view
urlpatterns = [
    path('login/', login_view, name = "login_view"),
    path('register/', register_view, name = "register_view"),
    path('logout/', logout_view, name = "logout"),
    path("messages/<int:id>", messages_view, name = "messages"),
    path("sendmessage/<int:userId>&<int:restId>", send_message_view, name = "send-message")
]