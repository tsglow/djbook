from django.contrib import admin
from .models import Book, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):    
    prepopulated_fields = {"url": ("title",) }
    list_filter = ("author", "rating")
    list_display = ("title", "author")

class AuthorAdmin(admin.ModelAdmin):        
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name")

admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)
