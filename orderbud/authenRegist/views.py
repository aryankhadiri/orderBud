from django.shortcuts import render
from .forms import registerForm, LoginForm
# Create your views here.
def login_view(request):
    #TODO login view
    form = LoginForm()
    context = {
        "form":form
    }
    return render (request, "login.html", context)

def register_view(request):
    #TODO register view
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')

    else:
       form = registerForm()

       content = {'form': form}
       return render(request, 'register.html', content)
   