from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def homepage(request):
      return render(request , 'marvels.html')
      
def allmovies(request):
     movies=Movie.objects.all()   
     comp=Production_company.objects.all() 
     direct=Director.objects.all()
     produce=Producer.objects.all()
     act=Actor.objects.all() 
     connector=Connector.objects.all()
    
     context = {
                    'comp':comp,
	                'movies':movies,
	                'direct':direct,
	                'produce':produce,
	                'connector':connector,
	                'act':act
	             }
     con=loader.get_template('allmovies.html')
     
     return HttpResponse(
	              con.render(context , request)
	)
	
	

def ironman(request):
	  return render (request , 'Ironman.html')

def captainamerica(request):
	  return render (request , 'captainamerica.html')
	
def thor(request):
	  return render (request , 'Thor.html')
	
def hulk(request):
	  return render (request , 'hulk.html')
	
def avengers(request):
	  return render (request , 'Avengers.html')

def spiderman(request):
	  return render (request , 'spiderman.html')
	
def blackpanther(request):
	  return render (request , 'blackpanther.html')
	
def doctorstrange(request):
	  return render (request , 'doctorstrange.html')
	
def antman(request):
	  return render (request , 'antman.html')
	
def guardians(request):
	  return render (request , 'guardians.html')
	
def captainmarvel(request):
	  return render (request , 'captainamerica.html')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	