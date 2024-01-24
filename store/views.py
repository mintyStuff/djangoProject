from store.book_service import rent_book, return_book
from store.serializers import AuthorSerializer, BookSerializer, UserSerializer
from rest_framework import mixins, generics
from . models import User, Author, Book
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AuthorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookRentable(APIView):
    def get(self, request):
        book = Book.objects.all().filter(user=None).distinct()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

class BookRent(APIView):

    def put(self, request, bookId, userId):
        update_book = rent_book(bookId, userId)
        update_book.save()
        serializer = BookSerializer(update_book)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BookReturn(APIView):
        
    def put(self, request, returnedBookId):
        update_book = return_book(returnedBookId)
        update_book.save()
        serializer = BookSerializer(update_book)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
