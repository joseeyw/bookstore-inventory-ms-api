from rest_framework import generics, status
from ..models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

class BooksListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AddAuthorView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succcess":True})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
            

class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AddBookView(generics.CreateAPIView):
    serializer_class = BookSerializer
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(
            data=request.data
        )
        
        print( serializer.initial_data)
        stock_count = int(serializer.initial_data['stock_count'])
        if stock_count== 0:
            serializer.initial_data['stock_status'] = "Out of stock"
        elif stock_count > 0 and stock_count<=5:
            serializer.initial_data['stock_status'] = "Critical"
        elif stock_count > 5 and stock_count<=10:
            serializer.initial_data['stock_status'] = "Bad"
        elif stock_count > 10:
            serializer.initial_data['stock_status'] = "Good"

        print(serializer)
        if serializer.is_valid():  # will call the validate function
            serializer.save()
            return Response({'success': True})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        