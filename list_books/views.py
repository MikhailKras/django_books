from django.shortcuts import render
from .models import Books
# Create your views here.


def get_list_books(request):
    data = {
        'books': Books.objects.all()
    }
    return render(request, 'list_books/list_books.html', context=data)
