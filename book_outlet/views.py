from django.shortcuts import render
from book_outlet.models import Book
from django.utils.text import slugify

# Create your views here.

def dbtodict():
    list = Book.objects.all()
    book_list = []
    for b in list:        
        book_list.append({
            "title": b.title,
            "author": b.author,
            "rating": b.rating,
            "is_bestselling": b.is_bestselling,
            "url": slugify(b.title)
            })
    return book_list

def get_detail(url):
    book_list = dbtodict()
    result = next((book for book in book_list if book["url"] == url))    
    return result


def index(request):
    return render(request,"book_outlet/index.html", {"books": dbtodict()})

def detail(request,url):
    return render(request, "book_outlet/detail.html", {"book": get_detail(url)})