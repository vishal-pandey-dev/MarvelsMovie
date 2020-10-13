from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Character(models.Model):
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	image=models.ImageField(upload_to='pics')
	desc=models.CharField(max_length=500)
	
	def __str__(self):
		return self.name
		
class Phase(models.Model):
	name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
	
	
class Movie (models.Model):
	character=models.ForeignKey(Character, on_delete=models.CASCADE)
	phase=models.ForeignKey(Phase, on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	imdb=models.FloatField(default=0)
	rotten=models.IntegerField(default=0)
	image=models.ImageField(upload_to='pics')
	runtime=models.IntegerField(default=0)
	language=models.CharField(default='English',max_length=20)
	collection=models.FloatField(default=0)
	release=models.DateField()
	trailer=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
class Production_company(models.Model):
	movie=models.ForeignKey(Movie, on_delete=models.CASCADE, default='Marvels Studio')
	name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
class Producer(models.Model):
	movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
class Director(models.Model):
	movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
	
class Actor(models.Model):
	name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.name
		
class Connector(models.Model):
	movie=models.ForeignKey(Movie, on_delete=models.CASCADE)
	actor=models.ForeignKey(Actor, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.movie
		

	



	



