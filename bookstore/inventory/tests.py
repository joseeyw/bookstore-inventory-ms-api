import json
from django.test import TestCase, Client
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User
from inventory.models import Author, Book

# Create your tests here.

class AuthorTestCase(TestCase):
    def setUp(self):
        # create Author
        self.client = Client()
        self.first_name ="John"
        self.last_name ="Doe"
        self.email = "test1@example.com"
        self.date_of_wrong_format_birth = '18/09/19'
        self.date_of_birth ="2018-09-10"

        self.username = "test"
        self.password = "string"

        User.objects.create_user(username=self.username, email=self.email, password=self.password)
        response = self.client.post(reverse('auth:login'), {"username": self.username, "password": self.password})
        
        self.token = response.json()['token']

        self.headers={'HTTP_AUTHORIZATION':f'Token {self.token}'}
        


    def test_sucess_author_creation(self):
        response = self.client.post(reverse('inventory:author_add'),  {"first_name": self.first_name, "last_name": self.last_name, "email": self.email, "date_of_birth":self.date_of_birth }, **self.headers)
        
        self.assertEqual(response.status_code, 201)

    def test_fail_author_creation_wrong_format(self):
    
        response = self.client.post(reverse('inventory:author_add'),  {"first_name": self.first_name, "last_name": self.last_name, "email": self.email, "date_of_birth":self.date_of_wrong_format_birth }, **self.headers)
       
        self.assertEqual(response.status_code, 400)
        
    def test_success_get_all_authors(self):
        response = self.client.get(reverse('inventory:author_list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_author(self):
        author = Author.objects.create(first_name=self.first_name, last_name=self.last_name, email=self.email, date_of_birth=self.date_of_birth)
        response = self.client.get(reverse('inventory:author_detail', kwargs={'pk':author.id}))
        self.assertEqual(response.status_code, 200)

        
class BookTestCase(TestCase):
    def setUp(self):
        # create Author
        self.client = Client()
        self.first_name ="John"
        self.last_name ="Doe"
        self.email = "test1@example.com"
        self.date_of_wrong_format_birth = '18/09/19'
        self.date_of_birth ="2018-09-10"

        self.author = Author.objects.create(first_name=self.first_name, last_name=self.last_name, email=self.email, date_of_birth=self.date_of_birth)

        self.title = "Test Book",
        self.year_of_publication =2000
        self.stock_count= 20
        self.author_id = self.author.id
    #TODO Imutability issue
    # def test_sucess_book_creation(self):
    #     print("The auther id", self.author.id)
    #     response = self.client.post(reverse('inventory:books_add'), {"title": self.title, "year_of_publication": self.year_of_publication, "stock_count": self.stock_count, "author": self.author.id}, type='json')
    #     print(response.json())
    #     self.assertEqual(response.status_code, 201)
        
    def test_success_get_all_books(self):
        response = self.client.get(reverse('inventory:books_list'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_book(self):
        book = Book.objects.create(title =self.title, year_of_publication=self.year_of_publication, stock_count=self.stock_count, author=self.author)
        response = self.client.get(reverse('inventory:books_detail', kwargs={'pk':book.id}))
        self.assertEqual(response.status_code, 200)

class StockHistory(TestCase):
    def setUp(self):
        self.client = Client()
        # create Author
        self.client = Client()
        self.first_name ="John"
        self.last_name ="Doe"
        self.email = "test1@example.com"
        self.date_of_wrong_format_birth = '18/09/19'
        self.date_of_birth ="2018-09-10"

        self.author = Author.objects.create(first_name=self.first_name, last_name=self.last_name, email=self.email, date_of_birth=self.date_of_birth)

        self.title = "Test Book",
        self.year_of_publication =2000
        self.stock_count= 20
        self.author_id = self.author.id

        self.book = Book.objects.create(title =self.title, year_of_publication=self.year_of_publication, stock_count=self.stock_count, author=self.author)

    # def test_success_get_all_stock_history(self):
    #     response = self.client.get(reverse('inventory:books_list'))
    #     self.assertEqual(response.status_code, 200)

    # def test_detail_view_book(self):
    #     book = Book.objects.create(title =self.title, year_of_publication=self.year_of_publication, stock_count=self.stock_count, author=self.author)
    #     response = self.client.get(reverse('inventory:books_detail', kwargs={'pk':book.id}))
    #     self.assertEqual(response.status_code, 200)
