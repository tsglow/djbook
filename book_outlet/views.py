from django.shortcuts import render
from book_outlet.models import Book
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Avg, Max, Min

# Create your views here.

def dbtodict():
    list = Book.objects.all().order_by("-rating")        
    return list

def get_detail(url):
    book = Book.objects.get(url=url)    
    return book

def index(request):
    books = dbtodict()
    num_books = books.count()
    avg_rating = books.aggregate(Avg("rating"))

    return render(request,"book_outlet/index.html", {
        "books": books,
        "total": num_books,
        "average": avg_rating
        })

def detail(request,pk,url):        
    try:
        book = get_detail(url)
        return render(request, "book_outlet/detail.html", {"book": book})
    except:
        raise Http404()
    
def detail_id(request,pk):
    try:
        slug = Book.objects.get(pk=pk).url
        re_path = reverse("detail", args=[pk, slug])
        return HttpResponseRedirect(re_path)
    except:
        raise Http404()    
    