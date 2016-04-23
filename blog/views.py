from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def home(request):
    return render(request, "index.html")

def post_management(request):
    data = {"working_title": "New Blog Post", "working_content": "Blog content goes here..."}
    return render(request, "post_management_view.html", data)

def post_preview(request):
    data = {"title": request.POST["title"], "content": request.POST["content"]}
    return HttpResponse(render_to_string("post_view.html", data))
