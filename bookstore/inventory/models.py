from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50, required=True)
    last_name = models.CharField(max_length=50, required=True)
    email = models.EmailField(max_length=200, required=True)
    date_of_birth = models.DateField(required=True)    

class Book(models.Model):
    title = models.CharField(max_length=200, required=True)
    year_of_publication = models.IntegerField(required=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, required=True)