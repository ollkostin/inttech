from django.db.models.functions import Lower
from django.shortcuts import render
from library.models import Book, Genre, Author

SORT = "book_name_sort"
GENRES = "genre_ids"
AUTHORS = "author_ids"


def index(request):
    context = {
        "genres": Genre.objects.all(),
        "authors": Author.objects.all()
    }

    genre_ids = [int(el) for el in request.GET.getlist('genre')]
    author_ids = [int(el) for el in request.GET.getlist('author')]
    book_name_sort = request.GET.get(SORT)
    if len(genre_ids) != 0 and len(author_ids) != 0:
        result = Book.objects.filter(genre__id__in=genre_ids, author__id__in=author_ids)
    elif len(genre_ids) != 0:
        result = Book.objects.filter(genre__id__in=genre_ids)
    elif len(author_ids) != 0:
        result = Book.objects.filter(author__id__in=author_ids)
    else:
        result = Book.objects.all()

    if book_name_sort == 'asc':
        result = result.order_by(Lower('name').asc())
    else:
        result = result.order_by(Lower('name').desc())

    context["data"] = result
    context[SORT] = book_name_sort
    context[GENRES] = genre_ids
    context[AUTHORS] = author_ids
    return render(request, 'index.html', context)
