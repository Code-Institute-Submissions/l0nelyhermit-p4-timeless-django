from django.urls import path
from .views import index, create_post, show_post, edit_post, delete_post

urlpatterns = [
    path('', index, name='index'),
    path('create_post', create_post, name='create_post'),
    path('show_post', show_post, name='show_post'),
    path('edit_post/<item_id>', edit_post, name='edit_post'),
    path('delete_post/<item_id>', delete_post, name='delete_post'),
]
