"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from . import views
from .views import BookDetailSlugView


urlpatterns = [
    #  path('',views.home, name='home' ),
    # path('',views.bookButton, name='book' ),

    path('',views.book_list_view, name='homepage'),
    re_path('home/(?P<slug>[\w-]+)/$',BookDetailSlugView.as_view()),

    # re_path('(?P<slug>[\w-]+)/$',BookDetailSlugView.as_view()),  create conflict with other below url through booksdetailslugview.. TexasInnovator,Bookify,mitrapark




    path('plustwo/',views.plustwo,name='plustwo'),
    path('bachelor/',views.bachelor,name='bachelor'),
    path('school/',views.school,name='school'),
    path('see/',views.see,name='see'),
    path('diploma/',views.diploma,name='diploma'),
    path('master/',views.master,name='master'),
    path('extra/',views.extra,name='extra'),
    path('new_collections/',views.new_collections,name='new_collections'),
    path('donations/',views.donations,name='donations'),






       




]
