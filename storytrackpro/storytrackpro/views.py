from django.shortcuts import render
from .sql_queries import *

def homepage_view(request):
    template_name = 'homepage.html'
    return render(request, template_name)

def dashboard_view(request):
    template_name = 'dashboard.html'
    query = "SELECT * FROM STORY;"
    stories = execute_query(query)
    return render(request, template_name, {'stories': stories})

def assignments_view(request):
    template_name = 'assignments.html'
    return render(request, template_name)

def status_view(request):
    template_name = 'status.html'
    return render(request, template_name)

def submit_view(request):
    template_name = 'submit.html'
    return render(request, template_name)