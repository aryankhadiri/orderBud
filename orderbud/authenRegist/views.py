from django.shortcuts import render
from .forms import registerForm, LoginForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
# Create your views here.
def login_view(request):
    #TODO login view
    if request.method == "POST":
        print(request.POSt)
    form = LoginForm()
    context = {
        "form":form
    }
    
    return render (request, "login.html", context)

def register_view(request):
    #TODO register view
    if request.method == "POST":
        form2 = registerForm(request.POST, request.FILES)
        if form2.is_valid():
            form2.save()
            success_message = "User profile has been saved successfully."
            messages.success(request, success_message)
        else:
            messages.error(request, form2.errors)
    form = registerForm()
    context = {
        "form": form
    }

    return render (request, "register.html", context)