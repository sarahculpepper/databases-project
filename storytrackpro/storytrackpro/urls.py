from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage_view, name='home'),
    path('home/', homepage_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('assignments/', assignments_view, name='assignments'),
    path('story-status/', status_view, name='status'),
    path('submit-story/', submit_view, name='submit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


