from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email, URLValidator
from .models import Author, Book
from django.contrib.auth.models import User



# class ArtistCreateForm (forms.ModelForm):
#     class Meta:
#         model = Artist
#         fields = '__all__'#['name', 'genre', 'year']
#
#
#
# class AlbumCreateForm (forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'#['name', 'artist_album', 'year']
#
#
#
# class MovieCreateForm (forms.ModelForm):
#     class Meta:
#         model = Movie
#         fields = '__all__'



class AuthorCreateForm (forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class BookCreateForm (forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'year', 'category', 'description', 'isbn', 'available')
