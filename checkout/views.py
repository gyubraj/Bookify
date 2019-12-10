from django.shortcuts import render
from . models import CheckOut
from django.conf import settings
from django.contrib.auth.models import User
from addBook.models import Book
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def checkout(request,id):
    book=Book.objects.get(id=id)
    buyerid=request.user.id
    sellerid=book.bookowner
    





    if(buyerid == sellerid):
        msg="Sorry you can't Buy this book sice this is your own book"
        return render(request,"checkout.html",{'data':msg})

    else:
        if (book.status=="pending"):
            msg="You have already order this Book. Check you Gmail for more detail",
            return render(request,"checkout.html",{'data':msg})
        
        else:
            

            check=CheckOut(sellerid=sellerid, buyerid=buyerid, bookid=id, status="pending")
            check.save()
            msg='Thank you. Transaction has been Completed Successfully. Check out gmail for more detail'
            
            book.status="pending"
            book.buyerid=buyerid
            book.save()

        
            subject='Book Transaction Bookify'
            # sellerName=request.user.username(id=sellerid)
            seller=User.objects.get(id=sellerid)
            sellerName=seller.username
            buyerName=request.user.username
            messageSeller=render_to_string('book_transaction_email.html',
                        {'person':sellerName,
                        'action':'sell',
                        'bname':book.bname,
                        'category':book.category,
                        'ActionDo':'Buyer',
                        'secondPerson':buyerName,
                        'price':book.selling_price,
                        'publication':book.publication,
                        'things':'Book matching with above detail',
                        'limit':'within 5',
                            })
            from_email=[settings.EMAIL_HOST_USER]
            to_email=[seller.email]
            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=messageSeller, fail_silently=False)




            messageBuyer=render_to_string('book_transaction_email.html',
                        {'person':buyerName,
                        'action':'buy',
                        'bname':book.bname,
                        'category':book.category,
                        'ActionDo':'Seller',
                        'secondPerson':sellerName,
                        'price':book.display_selling_price,
                        'publication':book.publication,
                        'things':'above display fixed price',
                        'limit':'after 5',
                            })
            from_email=[settings.EMAIL_HOST_USER]
            to_email=[request.user.email]
            send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=messageBuyer, fail_silently=False)

        
        
            return render(request,"checkout.html",{'data':msg})

    


