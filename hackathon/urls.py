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
from django.contrib import admin
from django.urls import path,include,re_path

from django.conf import settings
from django.conf.urls.static import static

# from homepage.views import BookDetailSlugView,book_list_view,plustwo,bachelor,school,see,diploma,extra,master
from search.views import searchposts



urlpatterns = [
    path('admin/', admin.site.urls),
    #  path('data/',include('homepage.urls')),
    path('addbook/',include('addBook.urls')),

    path('profile/',include('UserProfile.urls')),



    # path('home/',book_list_view),
    path('',include('homepage.urls')),




    path('search/',searchposts,name='searchposts'),


    path('checkout/',include('checkout.urls')),
 

     path('registration/', include('registration.urls')),

     path('accounts/', include('django.contrib.auth.urls')),

     path('cartwork/',include('cart.urls')),


    
]

urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
