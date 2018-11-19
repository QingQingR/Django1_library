from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.urls import reverse
from django.utils import timezone
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponse("hello world!")

def detail(request):
    book_list=Book.objects.order_by('pub_date')[:5]
    context={'book_list': book_list}
    return render(request,'lib/detail.html',context)

def addBook(request):
    if request.method == 'POST':
        temp_name=request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']

    temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
    temp_book.save()
    #重定向
    return HttpResponseRedirect(reverse('libra:detail'))

def deleteBook(request,book_id):
    book_ID=book_id
    Book.objects.filter(id=book_ID).delete()
    return HttpResponseRedirect(reverse('libra:detail'))

def updateBook(request):
    if request.method == 'POST':
        temp_name=request.POST['name']
        temp_author = request.POST['author']
        temp_pub_house = request.POST['pub_house']
    if Book.objects.filter(name=temp_name):
        Book.objects.filter(name=temp_name).delete()
        temp_book = Book(name=temp_name, author=temp_author, pub_house=temp_pub_house, pub_date=timezone.now())
        temp_book.save()
        return HttpResponseRedirect(reverse('libra:detail'))


