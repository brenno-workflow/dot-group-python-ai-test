
from django.urls import path
from .views import GetBookView, PostBookView

# Lista de urls
urlpatterns = [
    path("books/create/", PostBookView.as_view(), name="book-create"),
    path("books/search/", GetBookView.as_view(), name="book-search"),
]