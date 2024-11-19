from django.shortcuts import redirect, render
from .sql_queries import *

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect("register")

    return render(request, "register.html")

def homepage_view(request):
    template_name = 'homepage.html'
    return render(request, template_name)

def dashboard_view(request):
    template_name = 'dashboard.html'
    query = "SELECT * FROM STORY;"
    stories = execute_query(query)
    if "assign_reporter" in request.POST:
        story_id = request.POST.get("story_id")
        reporter_id = request.POST.get("reporter_id")

        # Update the STORY table to assign the reporter
        query = """
            UPDATE STORY
            SET ReporterID = %s
            WHERE StoryID = %s;
        """
        execute_query(query, [reporter_id, story_id])

        # Update the stored info in reporters
        query = """
            SELECT id, username FROM auth_user;
        """
        reporters = execute_query(query)    
    return render(request, template_name, {'stories': stories})

def assignments_view(request):
    template_name = 'assignments.html'
    return render(request, template_name)

def status_view(request):
    template_name = 'status.html'
    return render(request, template_name)

def submit_view(request):
    template_name = 'submit.html'
    if request.method == "POST":
        # Get the form data from the request
        headline = request.POST.get("headline")
        status = request.POST.get("status")
        priority = request.POST.get("priority")
        assigned_date = request.POST.get("assigned_date")
        due_date = request.POST.get("due_date") 
        category = request.POST.get("category")
        story_body = request.POST.get("story_body")
        #reporter_id = request.user.id
        # SQL query to insert the new story
        query = """
            INSERT INTO STORY (Headline, Status, Priority, AssignedDate, DueDate, Category, StoryBody)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(query, [
                headline, status, priority, assigned_date, due_date, category, story_body#, reporter_id
            ])

        # Redirect to a success page or back to the dashboard
        return redirect("dashboard")  # Replace with the name of your dashboard route

    return render(request, template_name)