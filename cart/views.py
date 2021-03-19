from django.shortcuts import render, get_object_or_404
from watches.models import Watch
# Create your views here.


def cart(request, item_id):
    watch = get_object_or_404(Watch, pk=item_id)
    return render(request, 'cart.html', {
        'watch': watch
    })
