from django.shortcuts import render
from book_outlet.models import Book
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def dbtodict():
    list = Book.objects.all().order_by("-rating")        
    return list

def get_detail(url):
    book = Book.objects.get(url=url)    
    return book

def index(request):
    return render(request,"book_outlet/index.html", {"books": dbtodict()})

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
    