from rest_framework import serializers
from .models import Author, User, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class CreateBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'premierDate', 'printDate', 'author')
