from socketserver import UDPServer
from rest_framework import generics, status
from ..models import Author, Book
from .serializers import BookSerializer, BookCreateSerializer, AuthorSerializer
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.edit import UpdateView

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
        model = get_object_or_404(Book, pk=pk)
        # this is the only field we want to update
        stock_count = model.stock_count + int(stock)
        if stock_count== 0:
            stock_status= "Out of stock"
        elif stock_count > 0 and stock_count<=5:
            stock_status = "Critical"
        elif stock_count > 5 and stock_count<=10:
            stock_status = "Bad"
        elif stock_count > 10:
            stock_status = "Good"


        data = {"stock_count":stock_count, "stock_status":stock_status}
        serializer = BookSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AddStockView(APIView):

    def patch(self, request, pk, stock):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Book, pk=pk)
        # this is the only field we want to update
        stock_count = model.stock_count + int(stock)
        if stock_count== 0:
            stock_status= "Out of stock"
        elif stock_count > 0 and stock_count<=5:
            stock_status = "Critical"
        elif stock_count > 5 and stock_count<=10:
            stock_status = "Bad"
        elif stock_count > 10:
            stock_status = "Good"


        data = {"stock_count":stock_count, "stock_status":stock_status}
        serializer = BookSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveStockView(APIView):

    def patch(self, request, pk, stock):
        # if no model exists by this PK, raise a 404 error
        model = get_object_or_404(Book, pk=pk)
        # this is the only field we want to update
        stock_count = model.stock_count - int(stock)
        
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
            stock_count = 0


        data = {"stock_count":stock_count, "stock_status":stock_status}
        serializer = BookSerializer(model, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)