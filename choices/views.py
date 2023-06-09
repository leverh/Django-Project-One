from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

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

class ChoiceCreateView(LoginRequiredMixin, CreateView):
    model = models.Choice
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ChoiceUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Choice
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'choices/about.html', {'title': 'About'})
