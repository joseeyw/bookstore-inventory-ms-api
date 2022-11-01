from rest_framework import serializers
from ..models import Book,Author

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year_of_publication']