from django.shortcuts import render
from book_outlet.models import Book
from django.utils.text import slugify

# Create your views here.

def dbtodict():
    list = Book.objects.all().order_by("-rating")    
    for book in list:        
        book.url = slugify(book.title)            
    return list

def get_detail(url):
    list = dbtodict()
    result = next((book for book in list if book.url == url))    
    return result

def index(request):
    return render(request,"book_outlet/index.html", {"books": dbtodict()})

def detail(request,url):
    return render(request, "book_outlet/detail.html", {"book": get_detail(url)})