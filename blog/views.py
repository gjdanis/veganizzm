from django.shortcuts import render

def landing_view(request):
    return render(request, "index.html")

def header_view(request):
    return render(request, "header.html")