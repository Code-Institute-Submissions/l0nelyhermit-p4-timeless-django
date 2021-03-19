from django.shortcuts import render

# Create your views here.
def cart(request, item_id):
    return render(request, 'cart.html')