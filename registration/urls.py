from django.urls import path, re_path

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signup/account_activation_sent/',
         views.account_activation_sent, name='account_activation_sent'),
#     re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#             views.activate, name='activate'),

#     re_path('activate/^(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#             views.activate, name='activate'),

     re_path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
]
