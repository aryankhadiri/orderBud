from django import forms
from .models import RestPictures
from .models import FoodPictures
from .models import RestHours
from .models import Review
from .models import Nutritious

class RestPicForm(forms.ModelForm):
    class Meta:
        model = RestPictures
        fields = [
        	# 'pic_id',
        	# 'rest_id',
        	'pictures'
        ]


class FoodPicForm(forms.ModelForm):
	class Meta:
		model = FoodPictures
		fields = [
	         # 'pic_id',
	         # 'food_id',
	         'pictures'
	         ]

class HoursForm(forms.ModelForm):
	class Meta:
		model = RestHours
		fields = [
	              # 'hours_id',
	              # 'rest_id',
	              'day',
	              'oppening',
	              'close',
	              'time_frame'
	              ]

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = [
                  # 'review_id',
                  # 'rest_id',
                  # 'user_id',
                  # 'food_id',
                  'review',
                  'rating',
                  'timestamp'
                  ]

                                
class NutritiousForm(forms.ModelForm):
	class Meta:
		model = Nutritious
		fields = [
					# 'nutri_id',
					# 'food_id',
					'calories',
					'saturated_fat',
					'sodium',
					'sugar'
					]

	     
    	