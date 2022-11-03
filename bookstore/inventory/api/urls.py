from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('books/',  views.BooksListView.as_view(),  name = 'books_list'),
    path('books/<pk>/', views.BookDetailView.as_view(), name = 'books_detail'),
    path('books/author/<author_id>/', views.BooksPerAuthorListView.as_view(), name = 'books_list_author'),
    path('books/year/<publication_year>/', views.BooksPerPublicationYearListView.as_view(), name = 'books_list_year'),
    path('books/add',  views.AddBookView.as_view(),  name = 'books_add'),
    path('author/',  views.AuthorListView.as_view(),  name = 'books_list'),
    path('author/<pk>/', views.AuthorDetailView.as_view(), name = 'books_detail'),
    path('author/add',views.AddAuthorView.as_view(), name = 'author_add'),
    path('stock/add/<pk>/<int:stock>', views.AddStockView.as_view(), name = 'stock_add'),
    path('stock/remove/<pk>/<int:stock>', views.RemoveStockView.as_view(), name = 'stock_remove'),
    path('stock/history/',  views.StockHistoryListView.as_view(),  name = 'books_list'),
    path('stock/history/<pk>/', views.StockHistoryDetailView.as_view(), name = 'books_detail'),
    path('stock/<book_id>/history/', views.StockHistoryPerBook.as_view(), name = 'books_history'),


]