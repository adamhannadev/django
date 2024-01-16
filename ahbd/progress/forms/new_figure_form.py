from django import forms
from progress.models import Dance, Level

class NewFigureForm(forms.Form):
    figure_name = forms.CharField(max_length=100)
    element = forms.CharField(max_length=30)
    leader_description = forms.CharField(widget=forms.Textarea)
    follower_description = forms.CharField(widget=forms.Textarea)
    dance = forms.ModelChoiceField(queryset=Dance.objects.all())
    level = forms.ModelChoiceField(queryset=Level.objects.all())