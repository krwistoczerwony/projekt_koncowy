"""Projekt_koncowy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from system_biblioteczny.views import (
    AuthorCreateView, BookCreateView, BookListView, BookDeleteView, BookUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('album_create/', AlbumCreateView.as_view(), name='album_create'),
    # path('artist_create/', ArtistCreateView.as_view(), name='artist_create'),
    # path('movie_create/', MovieCreateView.as_view(), name='movie_create'),
    # path('album_list/', AlbumListView.as_view(), name='album_list'),
    # path('movie_list/', MovieListView.as_view(), name='movie_list'),
    path('', BookListView.as_view(), name='book_list'),
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('book_create/', BookCreateView.as_view(), name='book_create'),
    path('book_update/', BookUpdateView.as_view(), name='book_update'),
    path('book_delete/', BookDeleteView.as_view(), name='book_delete'),
]
