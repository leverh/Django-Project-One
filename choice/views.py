from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome Foodies</h1>")

def about(request):
    return HttpResponse("<h1>The best App around for people who like to cook!</h1>")
