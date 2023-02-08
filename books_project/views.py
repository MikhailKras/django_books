from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseNotFound


def get_home_page(request):
    data = {
        'urls': [['list_books', 'list of my books']]
    }
    return render(request, 'home/home.html', context=data)
