from django.shortcuts import redirect, render
from .sql_queries import *
from .create_reporter_editor import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
import time

def register_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        role = request.POST.get("role")

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        # Create the user
        try:
            user = User.objects.create_user(username=name, email=email, password=password)
            user.save()
            create_reporter_editor(user.username, user.id, role)
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("login")
        except Exception as e:
            messages.error(request, f"Error: {e}")
            return redirect("register")

    return render(request, "register.html")

def homepage_view(request):
    template_name = 'homepage.html'
    return render(request, template_name)

@login_required
def dashboard_view(request):
    template_name = 'dashboard.html'
    query = "SELECT * FROM STORY;"
    stories = execute_query(query)
    query = "SELECT ReporterID, Name FROM REPORTER;"
    reporters = execute_query(query)
    query = "SELECT EditorID, Name FROM EDITOR;"
    editors = execute_query(query)
    context = {'stories': stories, 'reporters': reporters, 'editors': editors}
    if request.method == "POST":
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
            messages.success(request, "Story Sucessfully Updated.")
            return redirect("dashboard")
        if "request_review" in request.POST:
            story_id = request.POST.get("story_id")
            editor_id = request.POST.get("editor_id")

            # Update the STORY table to assign the editor & change status
            query = """
                UPDATE STORY
                SET EditorID = %s, Status = 'Awaiting Review'
                WHERE StoryID = %s;
            """
            execute_query(query, [editor_id ,story_id])
            messages.success(request, "Story Sucessfully Updated.")
            return redirect("dashboard")
    return render(request, template_name, context)

@login_required
def assignments_view(request):
    template_name = 'assignments.html'
    user_id = request.user.id
    query = "SELECT ReporterID FROM REPORTER WHERE UserID = %s;"
    reporter = execute_query(query, [user_id])
    reporterID = reporter[0][0]
    query = "SELECT * FROM STORY WHERE ReporterID = %s;"
    stories = execute_query(query, [reporterID])
    return render(request, template_name, {'stories': stories})

@login_required
def status_view(request):
    template_name = 'status.html'
    query = "SELECT * FROM STORY;"
    stories = execute_query(query)
    if request.method == "POST":
        if "status_update" in request.POST:
            story_id = request.POST.get("story_id")
            status = request.POST.get("status")
            query = """
                UPDATE STORY
                SET Status = %s
                WHERE StoryID = %s;
            """
            execute_query(query, [status ,story_id])
            messages.success(request, "Story Sucessfully Updated")
            return redirect("status")
        if "submit_feedback" in request.POST:
            story_id = request.POST.get("story_id")
            feedback = request.POST.get("feedback")
            query = """
                UPDATE STORY
                SET Feedback = %s
                WHERE StoryID = %s;
            """
            execute_query(query, [feedback ,story_id])
            messages.success(request, "Feedback Submitted")
            return redirect("status")
    return render(request, template_name, {'stories': stories})

@login_required
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
        messages.success(request, "Story Sucessfully Created.")
        return redirect("dashboard")  # Replace with the name of your dashboard route

    return render(request, template_name)

@login_required
def story_view(request, id):
    template_name = 'story.html'
    query = "SELECT * FROM STORY WHERE StoryID = %s;"
    stories = execute_query(query, [id])
    if request.method == "POST":
        if "update_story" in request.POST:
            title = request.POST.get("title")
            story_body = request.POST.get("storybody")
            query = """
                UPDATE STORY
                SET Headline = %s, StoryBody = %s
                WHERE StoryID = %s;
            """
            execute_query(query, [title, story_body, id])
            messages.success(request, "Story Sucessfully Updated.")
            return redirect(reverse('story', kwargs={'id': id}))
        if "delete_story" in request.POST:
            query = """
            DELETE FROM STORY
            WHERE StoryID = %s;
            """
            execute_query(query, [id])
            messages.success(request, "Story Sucessfully Deleted.")
            return redirect("dashboard")
    return render(request, template_name, {'stories': stories})
