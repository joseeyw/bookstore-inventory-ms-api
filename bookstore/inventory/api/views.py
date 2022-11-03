from datetime import datetime
from socketserver import UDPServer
from rest_framework import generics, status
from ..models import Author, Book, StockHistory
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer, StockHistorySerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.edit import UpdateView
from rest_framework.permissions import IsAuthenticated

class BooksListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BooksPerAuthorListView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.filter(author=self.kwargs['author_id']).all()

class BooksPerPublicationYearListView(generics.ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):
        return Book.objects.filter(year_of_publication=self.kwargs['publication_year']).all()

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AddAuthorView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"succcess":True}, status.HTTP_201_CREATED)
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
    serializer_class = BookCreateSerializer
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(
            data=request.data
        )
        
        stock_count = int(serializer.initial_data['stock_count'])
        if stock_count== 0:
            serializer.initial_data['stock_status'] = "Out of stock"
        elif stock_count > 0 and stock_count<=5:
            serializer.initial_data['stock_status'] = "Critical"
        elif stock_count > 5 and stock_count<=10:
            serializer.initial_data['stock_status'] = "Bad"
        elif stock_count > 10:
            serializer.initial_data['stock_status'] = "Good"

        if serializer.is_valid():  # will call the validate function
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class AddStockView(APIView):

    def patch(self, request, pk, stock):
        # if no model exists by this PK, raise a 404 error
        book = get_object_or_404(Book, pk=pk)
        # this is the only field we want to update
        stock_count = book.stock_count + int(stock)
        timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        record = f"Added {stock} items at {timestamp}. New Stock Records {stock_count}"
        if stock_count== 0:
            stock_status= "Out of stock"
        elif stock_count > 0 and stock_count<=5:
            stock_status = "Critical"
        elif stock_count > 5 and stock_count<=10:
            stock_status = "Bad"
        elif stock_count > 10:
            stock_status = "Good"


        data = {"stock_count":stock_count, "stock_status":stock_status}
        serializer = BookSerializer(book, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            StockHistory.objects.create(book=book, record=record)
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveStockView(APIView):

    def patch(self, request, pk, stock):
        # if no model exists by this PK, raise a 404 error
        book = get_object_or_404(Book, pk=pk)
        # this is the only field we want to update
        stock_count = book.stock_count - int(stock)
        timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        record = f"Removed {stock} items at {timestamp}. New Stock Records {stock_count}"
        if stock_count== 0:
            stock_status= "Out of stock"
        elif stock_count > 0 and stock_count<=5:
            stock_status = "Critical"
        elif stock_count > 5 and stock_count<=10:
            stock_status = "Bad"
        elif stock_count > 10:
            stock_status = "Good"
        elif stock_count < 0:
            stock_status= "Out of stock"
            timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            record = f" Tried Removed {stock} items at {timestamp} .The available stock is less. Stock Records {stock_count}"
            stock_count = 0


        data = {"stock_count":stock_count, "stock_status":stock_status}
        serializer = BookSerializer(book, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            #Update the stock history table
            StockHistory.objects.create(book=book, record=record)
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockHistoryListView(generics.ListAPIView):
    queryset = StockHistory.objects.all()
    serializer_class = StockHistorySerializer

class StockHistoryDetailView(generics.RetrieveAPIView):
    queryset = StockHistory.objects.all()
    serializer_class = StockHistorySerializer   

class StockHistoryPerBook(generics.ListAPIView):
    serializer_class = StockHistorySerializer 
    def get_queryset(self):
        return StockHistory.objects.filter(book=self.kwargs['book_id']).all()
        # return a meaningful error response

    
        

