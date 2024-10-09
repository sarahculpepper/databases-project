from django.shortcuts import render

def homepage_view(request):
    template_name = 'homepage.html'
    return render(request, template_name)

def dashboard_view(request):
    template_name = 'dashboard.html'
    return render(request, template_name)

def assignments_view(request):
    template_name = 'assignments.html'
    return render(request, template_name)

def status_view(request):
    template_name = 'status.html'
    return render(request, template_name)

def submit_view(request):
    template_name = 'submit.html'
    return render(request, template_name)