from django import forms
from . import models

class AddBookForm(forms.ModelForm):
    model = models.Book
    fields = "__all__"