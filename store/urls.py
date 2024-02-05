from django.urls import path
from .views import UserList, DeleteUser, BookList, AuthorList, BookRent, BookReturn, BookRentable, BookOperations, Login, SignUp

app_name="store"

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('signup/', SignUp.as_view(), name="sign up"),
    path('users/', UserList.as_view(), name="User endpoints"),
    path('users/<int:userId>', DeleteUser.as_view(), name="Delete user"),
    path('authors/', AuthorList.as_view() , name="Author endpoints"),
    path('books/', BookList.as_view(), name="Book endpoints"),
    path('books/operations/', BookOperations.as_view(), name="Book endpoints"),
    path('books/rentable/',  BookRentable.as_view(), name="Rentable Book"),
    path('books/<int:returnedBookId>/return/', BookReturn.as_view(), name="Return Book"),
    path('books/<int:bookId>/user/<int:userId>/rent/', BookRent.as_view(), name="Rent book"),
]