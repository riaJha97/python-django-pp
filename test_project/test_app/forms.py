from django import forms
from .models import Movie, Cinema


class MovieForm(forms.Form):
    your_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Wade Wilson'
                                                                                            }))
    # movies = forms.ModelChoiceField()


class CinemaForm(forms.Form):
    def __init__(self, *args, **kwargs):
        movie_name = kwargs.pop('movie_name')
        super(CinemaForm, self).__init__(*args, **kwargs)
        # self.fields['available_cinemas'] = forms.ModelChoiceField()
