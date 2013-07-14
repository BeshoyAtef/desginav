from designav_www.models import *
from django.shortcuts import render_to_response, redirect, render
from django.http import HttpResponse
import datetime

def home(request):
    return render_to_response ('index.html')

def view_all_members(request):
	list_of_members = []
	list_of_members = Member.objects.all()
	return render(request, 'index.html', {'list_of_members': list_of_members})

def view_all_news(request):
	list_of_news = []
	list_of_news = News.objects.all()
	print list_of_news
	return render(request, 'index.html', {'list_of_news': list_of_news})

def view_all_projects(request):
	list_of_projects = []	
	list_of_projects = Project.objects.all()
	return render(request, 'index.html', {'list_of_projects': list_of_projects})

# def view_project(request):
# 	project_id = request.POST['id']
# 	desired_project = Project.objects.get(id=project_id)
# 	print desired_project
# 	return render(request, 'project.html', {'project_info': desired_project})