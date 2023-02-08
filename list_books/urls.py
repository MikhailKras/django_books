from django.urls import path
from . import views

urlpatterns = [
    path('list', views.get_list_books, name='list_books'),
]
