from django import forms
from .models import Movie

Genre_Choices = [
    ('genre_1', '코미디'), 
    ('genre_2', '공포'), 
    ('genre_3', '로맨스'),
]

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        widget=forms.Textarea(
            attrs={
                'class': 'my-title form-control',
                'placeholder': 'Title',
                'rows': 1,
                'cols': 100,
            }
        )
    )
    audience = forms.IntegerField(
        label='Audience',
        widget=forms.NumberInput(
            attrs={
                'class': 'my-audience form-control',
                'placeholder': 'Audience',
                'rows': 1,
                'cols': 100,
            }
        )
    )
    poster_url = forms.CharField(
        label='Poster url',
        widget=forms.Textarea(
            attrs={
                'class': 'my-url form-control',
                'placeholder': 'Poster url',
                'rows': 5,
                'cols': 100,
            }
        )
    )
    description = forms.CharField(
        label='Description',
        widget=forms.Textarea(
            attrs={
                'class': 'my-description form-control',
                'placeholder': 'Description',
                'rows': 5,
                'cols': 100,
            }
        )
    )
    score = forms.FloatField(
        label='Score',
        widget=forms.NumberInput(
            attrs={
                'class': 'my-score form-control',
                'step': '0.5',
                'min': '0',
                'max': '5',
                'placeholder': 'Score',
            }
        )
    )
    release_date = forms.DateField(
        label='Release date',
        widget=forms.NumberInput(
            attrs={
                'type': 'date',
                'class':'my-release_date form-control',
                'placeholder': '연도-월-일',
            }
        )
    )
    genre = forms.CharField(
        label='Genre',
        widget=forms.Select(
            choices=Genre_Choices,
            attrs={
                'class': 'my-genre form-control',
            }
        ),
    )
    class Meta:
        model = Movie
        fields = '__all__'