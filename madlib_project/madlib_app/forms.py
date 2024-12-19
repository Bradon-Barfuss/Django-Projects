# madlib_app/forms.py

from django import forms

class MadLibForm(forms.Form):
    noun = forms.CharField(label='Noun', max_length=100)
    verb = forms.CharField(label='Verb', max_length=100)
    adjective = forms.CharField(label='Adjective', max_length=100)
    adverb = forms.CharField(label='Adverb', max_length=100)
    place = forms.CharField(label='Place', max_length=100)
    famous_person = forms.CharField(label='Famous Person', max_length=100)
    color = forms.CharField(label='Color', max_length=100)


