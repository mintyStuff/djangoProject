from django.contrib import admin

from store.models import Author, Book, User

# Register your models here.
admin.site.register([Book, Author, User])