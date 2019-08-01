from django import forms
from .models import Photo, YoutubeVideo
from django.utils.translation import gettext_lazy as _


class PhotoSubmitForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['image', 'caption', 'date', 'artist', 'show']
        labels = {
            'date': _("Date (format: yyyy-mm-dd)")
        }


class VideoSubmitForm(forms.ModelForm):

    class Meta:
        model = YoutubeVideo
        fields = ['youtube_url', 'caption', 'date', 'artist', 'show']
        labels = {
            'date': _("Date (format: yyyy-mm-dd)")
        }
