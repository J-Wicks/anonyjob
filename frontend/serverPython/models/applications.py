from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Applications
# Create your views here.

def index(request):
	if request.method == 'GET':
		all_applications = Application.objects.all()
		for application in all_applications:
			print(application.coverLetter)
			return HttpResponse(all_applications)
	elif request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		return HttpResponse(body['coverLetter'])