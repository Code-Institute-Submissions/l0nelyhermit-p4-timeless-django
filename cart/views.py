from django.shortcuts import render, get_object_or_404, redirect, reverse
from watches.models import Watch
from django.conf import settings
import stripe

# Create your views here.


def cart(request, item_id):

    watch = get_object_or_404(Watch, pk=item_id)
    amount = watch.price * 100
    if request.method == 'GET':
        key = settings.STRIPE_PUBLISHABLE_KEY
        return render(request, 'cart.html', {
            'key': key,
            'amount': amount,
            'watch': watch
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY
        charge = stripe.Charge.create(
            amount=amount,
            currency='sgd',
            description='Payment made for transaction: '+watch.watch_brand+" "+watch.watch_model,
            source=request.POST['stripeToken']
        )
        return redirect(reverse('show_post'))
