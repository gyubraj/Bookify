from addBook.models import Book
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.conf import settings
from cart.models import Cart
from django.http import HttpResponseRedirect

# Create your views here.

@login_required
def addtocart(request,id):
    userid=request.user.id
    bookid=id
    book=Book.objects.get(id=bookid)
    cartcheck=Cart.objects.filter(userid=userid)
    already=False
    for data in cartcheck:
        if(bookid == data.bookid):
            already=True
    if(userid==book.bookowner):
        return render(request,'ownbook.html')
    if(already):
        return redirect('homepage')
    else:
        cart=Cart(userid=userid,bookid=bookid,bookname=book.bname,price=book.display_selling_price,image=book.image)
        cart.save()
        return redirect('homepage')

@login_required
def displaycart(request):
    userid=request.user.id
    cart=Cart.objects.filter(userid=userid)
    total=0
    for data in cart:
        total +=data.price
    return render(request,'displaycart.html',{'cart':cart,'total':total})

@login_required
def cartremove(request,id):
    Cart.objects.get(id=id).delete()
    return redirect('displaycart')