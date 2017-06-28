from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Postings
# Create your views here.

def index(request):
	if request.method == 'GET':
		all_postings = Postings.objects.all()
		for posting in all_postings:
			print(posting.coverLetter)
			return HttpResponse(all_postings)
	elif request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		return HttpResponse(body['positionTitle'])