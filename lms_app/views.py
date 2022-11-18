from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
contextt = {
        'books' : Book.objects.all(),
        'catg' : Category.objects.all(),
        'bookform' : BookForm(),
        'catForm' : CatagForm(),
        }

def books(request):

        return render(request,'pages/books.html',contextt)

def index(request):
        if request.method == 'POST':
                book_data = BookForm(request.POST,request.FILES)
                if book_data.is_valid():
                        book_data.save()                
                cata_data = CatagForm(request.POST)
                if cata_data.is_valid():
                        cata_data.save() 
                       
        return render(request,'pages/index.html',contextt)

def sidebar(request):
    return render(request,'parts/slidebar.html',contextt)
