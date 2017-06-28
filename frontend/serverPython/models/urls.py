from django.conf.urls import url

from . import users, companies, applications, postings

urlpatterns = [
	url(r'^users/', users.index, name='users'),
	url(r'^companies/', companies.index, name='companies'),
	url(r'^applications/', applications.index, name='applications'),
	url(r'^postings/', postings.index, name='postings'),
]