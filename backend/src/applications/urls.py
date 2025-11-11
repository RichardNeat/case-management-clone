# applications/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("submit/", views.submit_application, name="submit_application"),
    path("success/", views.application_success, name="application_success"),
    path("", views.view_applications, name="view_applications")
]
