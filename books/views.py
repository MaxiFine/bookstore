from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/book_list.html'


class BookDetailView(LoginRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book' # new
    template_name = 'books/book_detail.html'

