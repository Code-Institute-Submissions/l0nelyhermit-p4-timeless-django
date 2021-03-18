from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
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
    if request.method == "POST":
        # load the updated form from the html
        modified_form = WatchForm(request.POST, instance=watch_edited)
        if modified_form.is_valid():
            # process the form and save to database if it is valid
            form = modified_form.save(commit=False)
            form.save()
            return redirect(reverse(show_post))
        else:
            # return to form if invalid form
            return render(request, 'edit_post.html', {
                'form': modified_form
            })
    form = WatchForm(instance=watch_edited)
    return render(request, 'edit_post.html', {
        'form': form
    })
