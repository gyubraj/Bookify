from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, "others/about.html")


def terms(request):
    return render(request, "others/terms.html")
