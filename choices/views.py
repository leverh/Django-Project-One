from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView

# Create your views here.
def home(request):
    choices = models.Choice.objects.all()
    context = {
        'choices': choices
    }
    return render(request, 'choices/home.html', context)

class ChoiceListView(ListView):
    model = models.Choice
    template_name = 'choices/home.html'
    context_object_name = 'choices'
    ordering = ['-date_posted']

class ChoiceDetailView(DetailView):
    model = models.Choice

def about(request):
    return render(request, 'choices/about.html', {'title': 'About'})
