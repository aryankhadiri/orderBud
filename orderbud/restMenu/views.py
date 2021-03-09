from django.shortcuts import render
from .forms import RestPicForm
from .forms import HoursForm
from .forms import FoodPicForm
from .forms import NutritiousForm
from .forms import ReviewForm

# Create your views here.

def food_view(request):
	form = RestPicForm(request.Post or None)
	if form.is_valid():
		form.save()
		form = RestPicForm()

	context = {
		'form': form
	} return render(request, "food.html")
