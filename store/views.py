from store.book_service import rent_book, return_book
from store.serializers import AuthorSerializer, BookSerializer, UserSerializer, CreateBookSerializer
from rest_framework import mixins, generics
from . models import Author, Book # User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class SuperUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class Login(mixins.CreateModelMixin, generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response({"details": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(instance=user)
        return Response({"token": token.key, "user": serializer.data})



class SignUp(mixins.CreateModelMixin, generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({"token": token.key, "user": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    # authentication_classes = [SessionAuthentication, TokenAuthentication]
    # permission_classes = [IsAuthenticated&SuperUserOnly]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class DeleteUser(APIView):
    def delete(self, request, userId):
        User.objects.filter(id=userId).delete()
        return Response(status=status.HTTP_200_OK)

class AuthorList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookList(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class BookOperations(mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    serializer_class = CreateBookSerializer
    queryset = Book.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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
