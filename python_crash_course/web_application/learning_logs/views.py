from django.shortcuts import render

from .models import Project


def index(request):
    """The home page for learning log"""
    print("http response from index function.")
    return render(request, 'learning_logs/index.html')


def projects(request):
    """The page for displaying learning projects"""
    print("http response from learning_project function.")
    """
    projects = LearningProject.objects.order_by('start_date')
    context = {'Projects': projects}
    print(context)
    
    """
    return render(request, 'learning_logs/projects.html')