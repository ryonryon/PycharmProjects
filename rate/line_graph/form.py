from django.forms import ModelForm

from line_graph.models import RateData


class RateDataForm(ModelForm):
    class Meta:
        model = RateData
        fields = ('id', 'rate', 'datetime',)
