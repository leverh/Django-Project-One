from django.shortcuts import render, HttpResponse

choices = [
    {
    'author': 'John Doe',
    'title': 'Lentil Soup',
    'preparation' : 'mix all ingredients together and cook for 30 minutes',
    'date_posted': 'June 9, 2023'
    },
{
    'author': 'Mary Jane',
    'title': 'Vegan Burger',
    'preparation' : 'mix all ingredients together and cook for 30 minutes',
    'date_posted': 'June 11, 2023'
    },
    {
    'author': 'Angela Lansbury',
    'title': 'Hashbrown Casserole',
    'preparation' : 'mix all ingredients together and cook for 30 minutes',
    'date_posted': 'May 1, 2023'
    },
    {
    'author': 'Joan Collins',
    'title': 'Cucumber Salad',
    'preparation' : 'mix all ingredients together and cook for 30 minutes',
    'date_posted': 'January 9, 2023'
    }
]

# Create your views here.
def home(request):
    context = {
        'choices': choices
    }
    return render(request, 'choices/home.html', context)

def about(request):
    return render(request, 'choices/about.html', {'title': 'About'})
