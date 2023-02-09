from django.shortcuts import render, get_object_or_404
from .models import Books
# Create your views here.


def get_list_books(request):
    data = {
        'books': Books.objects.all()
    }
    return render(request, 'list_books/list_books.html', context=data)


def get_info_book(request, id_book: int):
    book = get_object_or_404(Books, id=id_book)
    data = {
        'book': book
    }
    return render(request, 'list_books/book.html', context=data)