from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def donate(request):
	return HttpResponse("You can donate")