from django.db import models
from django.utils.timezone import utc
from datetime import timedelta
import calendar
import datetime


class Project(models.Model):
	title = models.CharField(max_length=100)
	project_type = models.CharField(max_length=100)
	image = models.ImageField()

class Member(models.Model):
	name = models.CharField(max_length=100)
	job_description = models.CharField(max_length=100)
	email = models.EmailField(max_length=100, unique=True)

class Press(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField()

class News(models.Model):
	title = models.CharField(max_length=50)
	image = models.ImageField()
	text = models.CharField(max_length=1500)
	date = models.DateTimeField(default=datetime.datetime.now())

class CompanyInfo(models.Model):
	about_us = models.CharField(max_length=1000)
	email = models.EmailField(max_length=100, unique=True)
	address = models.CharField(max_length=1000)
	mobile = models.IntegerField(max_length=20)