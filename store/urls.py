from django.urls import path
from .views import UserList, BookList, AuthorList

app_name="store"

urlpatterns = [
    path('users/', UserList.as_view(), name="User endpoints"),
    path('authors/', AuthorList.as_view() , name="Author endpoints"),
    path('books/', BookList.as_view(), name="Book endpoints"),
    path('books/rentable',  BookList.as_view(), name="Rentable Book"),
    path('books/<int:bookId>/return', BookList.as_view(), name="Return Book"),
    path('books/<int:bookId>/user/<int:userId>/rent', BookList.as_view(), name="Rent book"),
]