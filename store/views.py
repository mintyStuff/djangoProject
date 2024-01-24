from store.book_service import rent_book, return_book
from store.serializers import AuthorSerializer, BookSerializer, UserSerializer
from rest_framework import mixins, generics
from rest_framework.decorators import action
from . models import User, Author, Book


class UserList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AuthorList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  generics.GenericAPIView):
                  
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_rentable(self, request, *args, **kwargs):
        filtered_queryset = self.queryset.filter(user=None).distinct()
        self.queryset = filtered_queryset
        return self.list(request, *args, **kwargs)

    def put_rent(self, request, bookId='None', userId='None', *args, **kwargs):
        update_book = rent_book(bookId, userId)
        request.data = update_book
        response = super().update(request, *args, **kwargs)
        return response

    @action(methods=['put'], detail=True, url_path='books/rent/', url_name='bla')
    def put_return(self, request, bookId='None', *args, **kwargs):
        book = return_book(bookId)
        request.data = book
        response = super().update(request, *args, **kwargs)
        return response