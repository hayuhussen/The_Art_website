from django.shortcuts import render
from django.urls import path
from .models import *
# Create your views here.
def index(request):
    banners = Banner.objects.all()
    nft_items = NFTItem.objects.all()
    categories = Category.objects.all()
    items = AboutSectionItem.objects.all()
    data = {
        "banners": banners,  # Changed key to "banners" to match template
        "nft_items":nft_items,
        "categories":categories,
        "items":items,
    }
    return render(request, "index.html", data)

def index2 (request):
    return render(request, "index-2.html")

def index3 (request):
    return render(request, 'index-3.html')

def index4 (request):
    return render(request, 'index-4.html')

def index5 (request):
    return render(request, 'index-5.html')
    
def login (request):
    return render(request, 'signin.html')
def collection(request):
    return render(request, 'collections.html')
def collection_single(request):
    return render(request, 'category-single.html')
def signup(request):
    return render(request, 'signup.html')
def homeblog(requset):
    return render(requset, 'blog.html')
def creator(request):
    return render(request, 'all-authors-2.html')
def contact(request):
    return render(request, 'contact.html')
def dashboard(request):
    return render(request, 'admindash/dashboard.html')
def userlist(request):
    return render(request, 'admindash/users.html')
def adminblog(request):
    return render(request, 'admindash/blog.html')
    