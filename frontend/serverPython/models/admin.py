from django.contrib import admin

# Register your models here.
from .models import User, Company, Postings, Applications

admin.site.register(User)

admin.site.register(Company)

admin.site.register(Postings)

admin.site.register(Applications)