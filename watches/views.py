from django.shortcuts import render, HttpResponse, redirect
from .models import Watch
from .forms import WatchForm

# Create your views here.


def index(request):
    return render(request, "index.html")


def create_post(request):
    if request.method == "POST":
        form = WatchForm(request.POST)
        print(form)
        return redirect(index)
    else:
        form = WatchForm()
        return render(request, "create_post.html", {
            'form': form
        })
