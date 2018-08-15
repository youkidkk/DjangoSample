from django import forms

class SampleForm(forms.Form):
    number = forms.IntegerField()
    string = forms.CharField()
    email = forms.EmailField()
    url = forms.URLField()
    date = forms.DateField()
    time = forms.TimeField()
    datetime = forms.DateTimeField()
    check = forms.BooleanField(required=False)

