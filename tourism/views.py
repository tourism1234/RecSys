from django.shortcuts import render
from django.http import HttpResponse
from .models import HillStations


def index(request):

	return HttpResponse("<h3> This will be the index page. </h3>")


def hillStations(request):

	all_hills = HillStations.objects.all()
	return render(request,'tourism/hillStations.html',{"all_hills":all_hills})


def details(request):
	all_hills = HillStations.objects.all()
	return render(request, 'tourism/details.html', {"all_hills": all_hills})
