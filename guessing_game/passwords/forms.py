from django import forms

class GuessPasswordForm(forms.Form):
    guess = forms.CharField(max_length=4, min_length=4, widget=forms.TextInput(attrs={'placeholder':'Password'}))