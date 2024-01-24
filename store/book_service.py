from store.models import Author, Book, User

MAX_RENTED_BOOKS = 3

def rent_book(bookID: int, userID: int):
    book = Book.objects.get(id=bookID)
    user = User.objects.get(id=userID)
    if not can_rent(user):
        raise Exception("User can only rent " + MAX_RENTED_BOOKS + " books.")
    else:
        book.user = user
        return book

def return_book(bookID: int):
    book = Book.objects.get(id=bookID)
    book.user = None
    return book

def can_rent(rentingUser: User):
    # does this notation with '__' work?
    return len(Book.objects.all().filter(user__id = rentingUser.id)) < MAX_RENTED_BOOKS