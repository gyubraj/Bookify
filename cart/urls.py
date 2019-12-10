
from django.urls import path
from . import views

urlpatterns = [
    #  path('',views.addBook, name='addBook' ),
    path('cart/<int:id>',views.addtocart, name='cart' ),
    path('cartview/',views.displaycart,name='displaycart'),
    path('removecart/<int:id>',views.cartremove,name='removecart'),

]
