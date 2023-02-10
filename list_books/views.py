from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from .models import Books
# Create your views here.


def get_list_books(request):
    books = Books.objects.all()
    total = books.aggregate(Count('id'))
    for book in books:
        book.save()
    data = {
        'books': books,
        'total': total
    }
    return render(request, 'list_books/list_books.html', context=data)


def get_info_book(request, slug_book: str):
    book = get_object_or_404(Books, slug=slug_book)
    data = {
        'book': book
    }
    return render(request, 'list_books/book.html', context=data)
