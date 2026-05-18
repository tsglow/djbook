from django.contrib import admin
from .models import Book, Author, Address, Country

# Register your models here.
class BookAdmin(admin.ModelAdmin):    
    prepopulated_fields = {"url": ("title",) }
    list_filter = ("author", "rating")
    list_display = ("title", "author")

class AuthorAdmin(admin.ModelAdmin):        
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name")

class AddressAdmin(admin.ModelAdmin):        
    list_filter = ("street", "city", "postal_code")
    list_display = ("street", "city", "postal_code")

class CountryAdmin(admin.ModelAdmin):        
    list_filter = ("name", "code")
    list_display = ("name", "code")

admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)

admin.site.register(Address, AddressAdmin)

admin.site.register(Country, CountryAdmin)
