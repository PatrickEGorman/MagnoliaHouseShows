from django import forms
from .models import History
from django.utils.translation import gettext_lazy as _


class HistoryForm(forms.ModelForm):

    class Meta:
        model = History
        fields = ["title", "text", "artists", 'shows', 'youtube_video', 'photo', 'flier', 'start_or_primary_date',
                  'end_date', 'approximate_date']
        labels = {
            'approximate_date': _('These dates are approximate'),
            'start_or_primary_date': _('Start or primary date (Format yyyy-mm-dd)')
        }