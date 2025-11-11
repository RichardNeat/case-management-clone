# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings

from .forms import ApplicationForm

from .models import Application

def submit_application(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/applications/success")
    else:
        form = ApplicationForm()

    return render(request, "application_form.html", {"form": form})

def application_success(request):
    return render(request, "application_success.html")

def view_applications(request):
    applications = Application.objects.all()
    for app in applications:
        if app.supporting_document:
            app.public_url = app.supporting_document.url.replace("http://minio:9000", settings.MINIO_PUBLIC_URL)
        else:
            app.public_url = None
    return render(request, "applications.html", {"applications": applications})