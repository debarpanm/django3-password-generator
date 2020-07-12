from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
	return render(request,'generator/home.html')

def password(request):

	chars = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('upperCase'):
		chars.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

	if request.GET.get('special'):
		chars.extend('!@#$%&*')

	if request.GET.get('numbers'):
		chars.extend('0123456789')

	length = int(request.GET.get('length'))
	thepassword = ''

	for i in range(length):
		thepassword+=random.choice(chars)
	
	return render(request,'generator/password.html',{'password':thepassword})

def credit(request):
	return render(request,'generator/credit.html')
