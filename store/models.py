from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=300)
    premierDate = models.DateField(null=True)
    printDate = models.DateField(null=True)
    author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.name

