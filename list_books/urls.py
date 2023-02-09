from django.urls import path
from . import views

urlpatterns = [
    path('list', views.get_list_books, name='list_books'),
    path('list/<int:id_book>', views.get_info_book, name='book-info')
]
