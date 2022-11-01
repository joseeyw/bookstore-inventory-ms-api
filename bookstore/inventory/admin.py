from django.contrib import admin
from inventory.models import Author, Book
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)