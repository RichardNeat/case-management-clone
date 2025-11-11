from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    context = {
        "title": "Welcome to the Case Management App Clone",
        "message": "This page is powered by Django running inside Docker.",
        "tech_stack": ["Django", "PostgreSQL", "MinIO", "Docker"],
    }
    return render(request, "hello.html", context)