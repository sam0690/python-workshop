from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'description': forms.Textarea(attrs={'class': 'form-control'}),
        #     'year': forms.NumberInput(attrs={'class': 'form-control'}),
        #     'genre': forms.Select(attrs={'class': 'form-control'}),
        #     'rating': forms.NumberInput(attrs={'class': 'form-control'}),
        # }