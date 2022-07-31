from django.urls import path

from . import views

urlpatterns = [
    path('addbook/', views.CreateBook.as_view(), name = 'addbook'),
    
]