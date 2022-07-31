from dataclasses import field
from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name = "Genre",
        max_length = 50
    )
    discription = models.TextField(
        verbose_name = "Genre discription",
        default = "Fill in the genre's discription"
    )
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(
        verbose_name = "Publisher",
        max_length = 50
    )
    discription = models.TextField(
        verbose_name = "Publisher discription",
        default = "Fill in the publisher's discription"
    )
    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(
        verbose_name = "Series title",
        max_length = 50
    )
    discription = models.TextField(
        verbose_name = "Series discription",
        default = "Fill series discription"
    )
    class Meta:
        verbose_name = "Series"
        verbose_name_plural = "Series"
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(
        verbose_name = "Author's name",
        max_length = 50
    )
    surname = models.CharField(
        verbose_name = "Author's surname",
        max_length = 50
    )
    biography = models.TextField(
        verbose_name = "Author's biography",
        default = "Fill in the author's biography"
    )
    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"
    def __str__(self):
        return self.surname

    
class Book(models.Model):
    name = models.CharField(
        verbose_name = "Book title",
        max_length = 50
    )
    photo = models.ImageField(
        verbose_name = "Cover photo",
        blank = True,
        
    )
    price = models.PositiveIntegerField(
        verbose_name = "Book price"
    )
    authors = models.ManyToManyField(
        Author,
        verbose_name = "Authors",
        related_name = "Books",
    )
    series = models.ForeignKey(
        Series,
        blank = True,
        on_delete = models.PROTECT
    )
    genres = models.ManyToManyField(
        Genre,
        verbose_name = "genres",
        related_name = "Books",
    )
    year_of_publication = models.PositiveIntegerField(
        verbose_name = "Year of publication"
    )
    pages = models.PositiveIntegerField(
        verbose_name = "Pages"
    )
    binding = models.CharField(
        verbose_name = "Book binding",
        max_length = 50
    )
    book_format = models.CharField(
        verbose_name = "Book format",
        max_length = 50
    )
    isbn = models.PositiveIntegerField(
        verbose_name = "ISBN"
    )
    weight = models.PositiveIntegerField(
        verbose_name = "Weight (grams)"
    )
    age_restrictions = models.PositiveIntegerField(
        verbose_name = "Age restrictions"
    )
    publishers = models.ForeignKey(
        Publisher,
        on_delete = models.PROTECT,
        verbose_name = "Publishers",
    )
    quantity = models.PositiveIntegerField(
        verbose_name = "Quantity",
    )
    activity = models.BooleanField(
        default = True,
        verbose_name = "Activity"
    )
    rating = models.PositiveIntegerField(
        verbose_name = "Rating",
        help_text = "Select a rating from 0 to 10"  
    )
    date_create = models.DateTimeField(
        auto_now_add = True,
        verbose_name = "Date create"
    )
    date_update = models.DateTimeField(
        auto_now = True,
        verbose_name = "Date update"
    )
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
    def __str__(self):
        return self.name