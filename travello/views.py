from django.shortcuts import render
from .models import Destination

# Create your views here.
def index(request):
    dest1 = Destination()
    dest1.name = 'newyork'
    dest1.dec = 'newyork is too beautiful city' 
    dest1.price = 799
    dest2 = Destination()
    dest2.name = 'berlin'
    dest2.dec = 'berlin is too beautiful city' 
    dest2.price = 899
    dest3 = Destination()
    dest3.name = 'switzerland'
    dest3.dec = 'switzerland is too beautiful city' 
    dest3.price = 999
    return render(request,'index.html',{'dest1': dest1,'dest2': dest2,'dest3': dest3})