from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	email = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	firstName = models.CharField(max_length = 24)
	lastName = models.CharField(max_length = 24)
	def __str__(self):
		return self.email

class Company(models.Model):
	companyName = models.CharField(max_length=200)
	HRemail = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	industry = models.CharField(max_length=200)
	def __str__(self):
		return self.HRemail

class Postings(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	positionTitle = models.CharField(max_length=200)
	positionDescription = models.CharField(max_length=2000)
	educationLevel = models.CharField(max_length=20)
	educationField = models.CharField(max_length=20, default='My Field')
	experienceField = models.CharField(max_length=20, default='My Field')
	experienceLevel = models.IntegerField(default=0)


class Applications(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	posting = models.ForeignKey(Postings, on_delete=models.CASCADE)
	coverLetter = models.CharField(max_length=2000)



