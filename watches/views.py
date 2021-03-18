from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Watch
from .forms import WatchForm


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


def edit_post(request, item_id):
    watch_edited = get_object_or_404(Watch, pk=item_id)
    form = WatchForm(instance=watch_edited)
    return render(request, 'edit_post.html', {
        'form': form
    })
