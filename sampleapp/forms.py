from django import forms

from .models import SampleModel


class SampleForm(forms.Form):
    number = forms.IntegerField()
    string = forms.CharField()
    email = forms.EmailField()
    url = forms.URLField()
    date = forms.DateField()
    time = forms.TimeField()
    datetime = forms.DateTimeField()
    check = forms.BooleanField(required=False)


class SampleModelForm(forms.ModelForm):
    class Meta:
        model = SampleModel
        fields = ["number", "text", "date", "time", "check"]
