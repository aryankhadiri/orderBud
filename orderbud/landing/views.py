from django.shortcuts import render

# Create your views here.
def landing_view(request):
    context = {'name':"Ayush"}
    return render(request, "landing.html", context)