from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User
from addBook.models import Book
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from checkout.models import CheckOut
# Create your views here.

@login_required
def profile(request):
    userprofile1 = User.objects.get(id=request.user.id)
    return render(request, 'profile/Profile.html', {'userProfile': userprofile1})

@login_required
def mybooks(request):
    book = Book.objects.filter(bookowner=request.user.id)
    book=reversed(book)
    return render(request, 'profile/mybooks.html', {'books': book})

@login_required
def onsell(request):
    book = Book.objects.filter(bookowner=request.user.id ,status ='available',donation=False)
    book=reversed(book)
    return render(request, 'profile/onsell.html', {'books': book})


# def editprofile(request):
#     userprofile1 = UserProfile.objects.get(id=4)
#     return render(request, 'editprofile.html', {'userProfile': userprofile1})

@login_required
def broughtbooks(request):
    book = Book.objects.filter(buyerid=request.user.id,status='clear')
    book=reversed(book)
    return render(request, 'profile/broughtbook.html', {'broughtbooks': book})

@login_required
def soldbooks(request):
    book = Book.objects.filter(bookowner=request.user.id ,status='clear')
    book=reversed(book)
    return render(request, 'profile/soldbooks.html', {'books': book})

@login_required
def donatedbooks(request):
    book=Book.objects.filter(bookowner=request.user.id,donation=True)
    book=reversed(book)
    return render(request,'profile/donatedbooks.html',{'books':book})
