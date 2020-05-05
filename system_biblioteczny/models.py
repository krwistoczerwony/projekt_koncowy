from django.db import models
from isbn_field import ISBNField


# MUSIC_GENRE = (
#     (1, 'Rock'),
#     (2, 'Metal'),
#     (3, 'Classical / Opera'),
#     (4, 'Soul / Blues'),
#     (5, 'Jazz'),
#     (6, 'Soundtrack'),
#     (8, 'Country'),
#     (9, 'Dance / Electronic / House'),
#     (10, 'Hip Hop / Rap / R&B'),
#     (11, 'Pop'),
#     (12, 'Audiobook')
# )
#
#
# MOVIE_GENRE = (
#     (1, 'horror'),
#     (2, 'kryminał'),
#     (3, 'sensacja'),
#     (4, 'sci fi'),
#     (5, 'dramat'),
#     (6, 'obyczaj'),
#     (7, 'muzyczny'),
#     (8, 'komedia'),
#     (9, 'dokument'),
#     (10, 'bajka'),
#     (11, 'koncert')
# )
#
#
# MUSIC_MEDIUM = (
#     (1, 'Vinyl'),
#     (2, 'CD')
# )
#
#
# MOVIE_MEDIUM = (
#     (1, 'BlueRay Disc'),
#     (2, 'DVD'),
#     (3, 'VHS'),
# )
#
#
#
#
# class Artist(models.Model):
#     name = models.CharField(max_length=64, unique=True, blank=None)
#     genre = models.IntegerField(choices=MUSIC_GENRE, blank=True)
#     year = models.SmallIntegerField(blank=True)
#
#     def __str__(self):
#         return self.name
#
#
#
# class Album(models.Model):
#     title = models.CharField(max_length=64, blank=None)
#     artist_album = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     year = models.SmallIntegerField(blank=True)
#     medium = models.IntegerField(choices=MUSIC_MEDIUM, blank=None, default=2)
#     available = models.IntegerField(choices=AVAILABLE, default=1)
#
#     def __str__(self):
#         return self.title
#
#
#
# class Movie(models.Model):
#     title = models.CharField(max_length=128, blank=None, null=None)
#     year = models.SmallIntegerField(blank=True)
#     medium = models.IntegerField(choices=MOVIE_GENRE)
#     category = models.IntegerField(choices=MOVIE_MEDIUM)
#     available = models.IntegerField(choices=AVAILABLE, default=1)
#
#     def __str__(self):
#         return self.title


###############



BOOK_CATEGORY = (
    (1, 'Horror'),
    (2, 'Kryminał'),
    (3, 'Sensacja'),
    (4, 'Romans'),
    (5, 'Biografia'),
    (6, 'Obyczaj'),
    (7, 'Muzyczny'),
    (8, 'Dokument i literatura faktu'),
    (9, 'Bajki dla dzieci'),
    (10, 'Sport i aktywnośc fizyczna'),
    (11, 'Podręcznik'),
    (12, 'Historyczno-przyrodnicza'),
    (13, 'Filozofia i nauki  scisłe'),
    (14, 'Atlasy i tablice naukowe'),
    (15, 'Prasa')
)



AVAILABLE = (
    ('Tak', 'Tak'),
    ('Nie', 'Nie')
)



class Author(models.Model):
    first_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=None)

    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name




class Book(models.Model):
    title = models.CharField(max_length=64, blank=None)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.SmallIntegerField(blank=True)
    category = models.IntegerField(choices=BOOK_CATEGORY, default=2)
    description = models.TextField(blank=True)
    isbn = ISBNField(blank=True)
    dirty_isbn = ISBNField(clean_isbn=False)
    available = models.IntegerField(choices=AVAILABLE, default=8)

    @property
    def book_title(self):
        return "{} {} {} rok wydania {}".format(self.author, self.title, self.year)

    def __str__(self):
        return self.book_title