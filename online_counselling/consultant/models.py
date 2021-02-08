from django.db import models
from django.contrib.auth.models import User
# Create your models here.

def phone_validator(value):
	if len(str(value)) == 10:
		pass
	else:
		raise ValidationError('Phone Number sholud be of 10 digits')


class Consultant(models.Model):
	"""Model for Consultant"""
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=80)
	last_name = models.CharField(max_length=80)
	phone_no = models.CharField(max_length=10,validators=[phone_validator])
	email_id = models.EmailField()
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	ratings = models.FloatField()
	number_of_reviews = models.IntegerField()
	number_of_customers = models.IntegerField()
	years_of_experience = models.IntegerField()
	type_of_consultant = models.CharField(max_length=150)
	date_of_birth = models.DateField()

	class Meta:
		db_table = 'consultant_details'


class ConsutancyType(models.Model):
	category_type = models.CharField(max_length=150)
	category_description = models.CharField(max_length=250)

	class Meta:
		db_table = 'consultancy_type'


class Portfolio(models.Model):
	consultant = models.ForeignKey(Consultant,on_delete=models.CASCADE)
	links = models.CharField(max_length=150)
