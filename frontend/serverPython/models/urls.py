from django.conf.urls import url

from . import index

urlpatterns = [
	url(r'^$', index.index, name='index'),
]