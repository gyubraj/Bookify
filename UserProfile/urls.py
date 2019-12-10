from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile, name='profile'),
    path('mybooks/', views.mybooks, name='mybooks'),
    path('onsell/', views.onsell, name='onsellbook'),
    #path('editprofile/', views.editprofile, name='editprofile'),
    path('broughtbooks/', views.broughtbooks, name='broughtbook'),
    path('soldbooks/', views.soldbooks, name='soldbooks'),
    path('donatedbooks/', views.donatedbooks, name='donatedbooks'),
    #path('editprofile/update/', views.infoupdate, name='update'),
]
