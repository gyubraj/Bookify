
from django.urls import path
from . import views


urlpatterns = [
    #  path('',views.addBook, name='addBook' ),
    path('checkout/<int:id>',views.checkout, name='checkout' ),




]
