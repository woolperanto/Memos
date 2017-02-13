from django.forms import ModelForm

from .models import Karte


class KarteForm(ModelForm):
    class Meta:
        model = Karte
        exclude = ('date_created', 'date_updated', 'author', 'showed_last_date',
                   'show_factor', 'times_known', 'times_showed')