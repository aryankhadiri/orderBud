from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import registerForm, LoginForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def login_view(request):
    print(list(messages.get_messages(request)))

    if request.method == "POST":
        email = request.POST.get("Email-text")
        password = request.POST.get("password-text")
        user = authenticate(request, username = email, password = password)
        if user is not None:
            login(request, user)
        else:
            messages.add_message(request, messages.ERROR, "Invalid Email/Password")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    


    form = LoginForm()
    context = {
        "form":form
    }
    
    return render (request, "login.html", context)

def register_view(request):
    print(list(messages.get_messages(request)))
    #TODO register view
    if request.method == "POST":
        form2 = registerForm(request.POST, request.FILES)
        if form2.is_valid():
            user = form2.save()
            success_message = "User profile has been saved successfully."
            messages.add_message(request, messages.SUCCESS, success_message)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))    
        else:
            for error in form2.errors:
                messages.add_message(request,messages.ERROR,form2.errors[error])

    form = registerForm()
    context = {
        "form": form
    }

    return render (request, "register.html", context)

def logout_view(request):
    if request.method=='POST':
        logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))    
     