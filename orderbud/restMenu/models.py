from django.db import models 

# Create your models here.

class Restaurant(models.Model):
	rest_id = models.CharField(max_length = 20,primary_key = True)
	username = models.CharField(max_length = 20)
	passaword = models.CharField(max_length = 20)
	rest_name = models.CharField(max_length = 50)
	rest_phone = models.PhoneNumberField()
	#image path needs to be specified later
	rest_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) 
	street = models.CharField(max_length = 50)
	city = models.CharField(max_length = 20)
	state = models.CharField(max_length = 10)
	zipcode = models.CharField(max_length = 20)
	rest_ratings = IntegerField()
	overall_rate = CharField(max_length = 20)


class User(models.Model):
	 user_id = models.CharField(max_length=20)
	 user_name = models.CharField(max_length=20)
	 email_addr = models.EmailField()
	 phone_number = models.PhoneNumberField()
	 #image path needs to be specified later
	 image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
	 rest_id = models.CharField(max_length=20)
	 

class Food(models.Model):
	FOOD_CATAGORY = [
			('AT','Appetizers'),
			('SL','Salads'),
			('SI','Side Items'),
			('EN','Entrees'),
			('BV','Beverages'),
	]

	food_id = models.CharField(max_length = 20, primary_key=True)
	rest_id = models.CharField(max_length = 20)
	name = models.CharField(max_length = 100)
	isvigen = models.BooleanField()
	isgfree = models.BooleanField()
	#image path needs to be specified later
	main_picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100) 
	description = models.TextField(max_length = 500)
	food_ratings = models.IntegerField()
	food_type = models.CharField(max_length = 20)
	food_catagory = models.CharField(max_length = 20, choice = FOOD_CATAGORY)
	overall_rate = models.CharField(max_length = 20)
	favorited = models.IntegerField()
	restaurant = models.ForeignKey('Restaurant',on_delete=models.CASCADE)

class RestPictures(models.Model):
	pic_id = models.CharField(max_length=20)
	rest_id = models.CharField(, max_length=20)
	#path?
	pictures = models.ImageField()


class FoodPictures(models.Model):
	pic_id = models.CharField( max_length=20)
	food_id = models.CharField(max_length=20)
	#path?
	pictures = models.ImageField()

class RestHours(models.Model):
	hours_id = models.CharField(max_length=20)
	rest_id = models.CharField(max_length=20)
	WEEKDAYS = [
    	('MON','Monday'),
    	('TUE','Tuesday'),
    	('WED','Wednesday'),
    	('THR','Thursday'),
    	('FRI','Friday'),
    	('SAT','Saturday'),
    	('SUN','Sunday'),
 	]
 	day = models.CharField(max_length=20, choice=WEEKDAYS)
 	openning = models.TimeField()
 	close = models.TimeField()
 	time_frame = models.CharField(max_length = 20, choices = (('AM','AM'),('PM','PM')), null=True, blank=True)

