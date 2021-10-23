"""Django URL patterns for learning_logs."""

from django.conf.urls import url

from . import views

urlpatterns = [
    # Home page
    # url('', views.index, name='index') is wrong
    # https://stackoverflow.com/questions/31056789/difference-between-and-in-urls-django
    url(r'^$', views.index, name='index'),

    # Show all learning projects
    # url(r'^projects/$', views.projects, name='projects'),
    url(r'projects/$', views.projects, name='projects'),

    # Detail page for a singe project
    url(r'^projects/(?P<project_id>\d+)/$', views.project, name='project')
]