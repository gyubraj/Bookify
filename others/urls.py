from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('terms/', views.terms, name='terms'),

]
