from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import User
# Create your views here.

def index(request):
	if request.method == 'GET':
		all_users = User.objects.all()
		for user in all_users:
			print(user.email)
			return HttpResponse(all_users)
	elif request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		return HttpResponse(body['email'])