from django.shortcuts import render, HttpResponse, redirect
from .models import Watch
from .forms import WatchForm

# Create your views here.


def index(request):
    return render(request, "index.html")

# create route for new watch listing


def create_post(request):
    if request.method == "POST":
        form = WatchForm(request.POST)
        form.save()
        return redirect(index)
    else:
        form = WatchForm()
        return render(request, "create_post.html", {
            'form': form
        })

# show all watches in listing


def show_post(request):
    watches = Watch.objects.all()
    return render(request, 'show_post.html', {
        'watches': watches
    })
