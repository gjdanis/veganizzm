from django.shortcuts import render

def recipe_management(request):
    return render(request, "post_management_view.html")

def recipe_preview(request):
    pass