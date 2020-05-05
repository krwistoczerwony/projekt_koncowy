from django.shortcuts import render
from .models import Book, Author
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, FormView
from .forms import AuthorCreateForm, BookCreateForm



# class AlbumCreateView(CreateView):
#     form_class = AlbumCreateForm
#     template_name = 'system_biblioteczny/form.html'
#     success_url = 'album_list/'
#
#
#
# class ArtistCreateView(CreateView):
#     form_class = ArtistCreateForm
#     template_name = 'system_biblioteczny/form.html'
#     success_url = 'album_list/'
#
#
#
# class MovieCreateView(CreateView):
#     form_class = MovieCreateForm
#     template_name = 'system_biblioteczny/form.html'
#     success_url = 'movie_list/'



# class AlbumListView(ListView):
#     queryset = Album.objects.all()
#     template_name = 'system_biblioteczny/album_list_form.html'
#
#
#
# class MovieListView(ListView):
#     queryset = Movie.objects.all()
#     template_name = 'system_biblioteczny/movie_list_form.html'




class AuthorCreateView(CreateView):
    form_class = AuthorCreateForm
    template_name = 'system_biblioteczny/form.html'
    success_url = ''



class BookCreateView(CreateView):
    form_class = BookCreateForm
    template_name = 'system_biblioteczny/form.html'
    success_url = ''



class BookListView(ListView):
    queryset = Book.objects.all()
    template_name = 'system_biblioteczny/book_list_form.html'



class BookDeleteView(DeleteView):
    model=Book
    template_name = "form.html"
    pk_url_kwarg = "book_id"
    success_url= '/'



class BookUpdateView(UpdateView):
    model = Book
    fields = ['title']
    pk_url_kwarg = 'book_id'
    template_name = '/book'
    success_url = '/'









