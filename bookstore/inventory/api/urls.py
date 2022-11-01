from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('books/',  views.BooksListView.as_view(),  name = 'books_list'),
    path('books/<pk>/', views.BookDetailView.as_view(), name = 'books_detail')
]