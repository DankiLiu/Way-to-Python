from django.shortcuts import render

from .models import Project


def index(request):
    """The home page for learning log"""
    print("http response from index function.")
    return render(request, 'learning_logs/index.html')


def projects(request):
    """The page for displaying learning projects"""
    print("http response from projects function.")

    projects = Project.objects.order_by('start_date')
    context = {'projects': projects}
    print(context)
    
    return render(request, 'learning_logs/projects.html', context)


def project(request, project_id):
    """The page for displaying single project"""
    print("http reponse from project function")

    project = Project.objects.get(id=project_id)
    entries = project.entry_set.order_by('date_added')
    context = {'project': project,
               'entries': entries}
    return render(request, 'learning_logs/project.html', context)