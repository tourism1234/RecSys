from django.shortcuts import render
from django.http import HttpResponse

def index(request):

	return HttpResponse("<h3> This will be the index page. </h3>")



