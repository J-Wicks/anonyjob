from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Company
# Create your views here.

def index(request):
	if request.method == 'GET':
		all_companies = Company.objects.all()
		for company in all_companies:
			print(company.companyName)
			return HttpResponse(all_companies)
	elif request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		return HttpResponse(body['companyName'])