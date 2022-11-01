from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    date_of_birth = models.DateField()   

    def __str__(self):
        return self.first_name + " "+ self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200)
    year_of_publication = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title