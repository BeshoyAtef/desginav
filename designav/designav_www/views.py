from designav_www.models import *
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
import datetime

def view_members(request):

	list_of_members = []
	list_of_members = Members.objects.all()
	print list_of_members

	return render(request, 'members.html', {'list_of_members': list_of_members})

def view_news(request):
	list_of_news = []
	list_of_news = News.objects.all()

	return render(request, 'news.html', {'list_of_news': list_of_news})

def view_all_projects(request):

	list_of_projects = []	
	list_of_projects = Projects.objects.all()

	return render(request, 'projects.html', {'list_of_projects': list_of_projects})

def view_project(request):

	project_id = request.GET['id']
	desired_project = Project.objects.get(id=project_id)

	return render(request, 'project.html', {'project_info': desired_project})