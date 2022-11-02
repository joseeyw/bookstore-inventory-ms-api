from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('books/',  views.BooksListView.as_view(),  name = 'books_list'),
    path('books/<pk>/', views.BookDetailView.as_view(), name = 'books_detail'),
    path('books/add',  views.AddBookView.as_view(),  name = 'books_add'),
    path('author/',  views.AuthorListView.as_view(),  name = 'books_list'),
    path('author/<pk>/', views.AuthorDetailView.as_view(), name = 'books_detail'),
    path('author/add',views.AddAuthorView.as_view(), name = 'author_add'),

    path('stock/add/<pk>/<stock>', views.AddStockView.as_view(), name = 'stock_add')

]