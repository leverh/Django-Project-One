from django.shortcuts import render, HttpResponse
from . import models
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    
class ChoiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Choice
    fields = ['title', 'description']

    def test_func(self):
        choice = self.get_object()
        if self.request.user == choice.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class ChoiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Choice
    success_url = '/'

    def test_func(self):
        choice = self.get_object()
        if self.request.user == choice.author:
            return True
        return False

def about(request):
    return render(request, 'choices/about.html', {'title': 'About'})
