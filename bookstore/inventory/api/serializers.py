from rest_framework import serializers
from ..models import Book,Author, StockHistory

class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        read_only_fields = ('stock_status',)
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class StockHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistory
        fields = '__all__'