

from . import forms
from django.shortcuts import render
from django.views.generic import CreateView

class CreateBook(CreateView):
    form = forms.AddBookForm
    template_name = "bookstore/addbook.html"

