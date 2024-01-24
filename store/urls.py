from django.urls import path
from .views import UserList, BookList, AuthorList, BookRent, BookReturn, BookRentable, BookCreat

app_name="store"

urlpatterns = [
    path('users/', UserList.as_view(), name="User endpoints"),
    path('authors/', AuthorList.as_view() , name="Author endpoints"),
    path('books/', BookList.as_view(), name="Book endpoints"),
    path('books/create/', BookCreat.as_view(), name="Book endpoints"),
    path('books/rentable/',  BookRentable.as_view(), name="Rentable Book"),
    path('books/<int:returnedBookId>/return/', BookReturn.as_view(), name="Return Book"),
    path('books/<int:bookId>/user/<int:userId>/rent/', BookRent.as_view(), name="Rent book"),
]