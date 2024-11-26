from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('', views.homepage_view, name='home'),
    path('home/', views.homepage_view, name='home'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('assignments/', views.assignments_view, name='assignments'),
    path('story-status/', views.status_view, name='status'),
    path('submit-story/', views.submit_view, name='submit'),
    path('dashboard/<int:id>/', views.story_view, name='story'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
