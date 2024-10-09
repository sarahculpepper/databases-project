from django.shortcuts import render

def homepage_view(request):
    template_name = 'homepage.html'
    return render(request, template_name)
