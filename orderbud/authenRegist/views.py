from django.shortcuts import render
from .forms import registerForm
# Create your views here.
def login_view(request):
    #TODO login view
    form = registerForm()
    context = {
        "form":form
    }
    return render (request, "login.html", context)

def register_view(request):
    #TODO register view
    print("ASD")