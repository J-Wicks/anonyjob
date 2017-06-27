from django.shortcuts import render
from django.http import HttpResponse

from .models import User
# Create your views here.

def index(request):
	all_users = User.objects.all()
	for user in all_users:
		print(user.email)
	return HttpResponse(all_users)