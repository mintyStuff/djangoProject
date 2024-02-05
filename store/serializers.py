from rest_framework import serializers
from .models import Author, Book # User
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'premierDate', 'printDate', 'author')
