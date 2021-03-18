from django import forms
from .models import Watch
from cloudinary.models import CloudinaryField


class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = (
            'watch_brand',
            'watch_model',
            'description',
            'price',
            'status',
            'cover'
        )
    cover = CloudinaryField()
