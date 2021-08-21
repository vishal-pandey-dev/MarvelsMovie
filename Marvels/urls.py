from django.urls import path
from . import views

urlpatterns=[
          path('', views.homepage,name='homepage'),
          path('allmovies', views.allmovies,name='allmovies'),
          path('ironman', views.ironman,name='ironman'),
          path('captainamerica', views.captainamerica,name='captainamerica'),
          path('thor', views.thor,name='thor'),
          path('hulk', views.hulk,name='hulk'),
          path('avengers', views.avengers,name='avengers'),
          path('spiderman', views.spiderman,name='spiderman'),
          path('blackpanther', views.blackpanther,name='blackpanther'),
          path('doctorstrange', views.doctorstrange,name='doctorstrange'),
          path('antman', views.antman,name='antman'),
          path('guardians', views.guardians,name='guardians'),
          path('captainmarvel', views.captainmarvel,name='captainmarvel'),          
]


