from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")


def create_post(request):
    return render(request, "create_post.html")
