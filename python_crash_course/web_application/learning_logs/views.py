from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Project
from .forms import ProjectForm, EntryForm


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


def new_project(request):
    """The page for adding a new project"""
    print("http response from new project function")
    if request.method != 'POST':
        # No data submitted; create a blank form
        print("Get")
        form = ProjectForm()
    else:
        # POST data submitted; process data
        print("Post")
        form = ProjectForm(request.POST)
        if form.is_valid():
            print("is valid")
            form.save()
            return HttpResponseRedirect(reverse('projects'))
    context = {'form:': form}
    return render(request, 'learning_logs/new_project.html', context)


def new_entry(request, project_id):
    """The page for adding a new entry"""
    print("http response from new entry function")
    project = Project.objects.get(id=project_id)
    if request.method != 'POST':
        # No data submitted; create a blank form
        print("Get")
        form = EntryForm()
    else:
        # POST data submitted; process data
        print("Post")
        form = EntryForm(request.POST)
        if form.is_valid():
            print("is valid")
            new_entry = form.save(commit=False)
            new_entry.project = project
            new_entry.save()
            return HttpResponseRedirect(reverse('project', args=[project_id]))
    context = {'project': project, 'form:': form}
    return render(request, 'learning_logs/new_entry.html', context)