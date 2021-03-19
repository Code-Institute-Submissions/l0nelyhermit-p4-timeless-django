from django.urls import path
from .views import cart

urlpatterns = [
    path('cart/<item_id>', cart, name='cart'),
]