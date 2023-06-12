from django.shortcuts import render, HttpResponse
from .models import Choice
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from .forms import ChoiceForm
from django.core.files.storage import default_storage
from cloudinary.forms import CloudinaryFileField
import cloudinary.uploader

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['title', 'description', 'preparation', 'picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['picture'].required = False

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        if picture:
            # Save the picture directly to the model instance
            self.instance.picture = picture
        return picture

def home(request):
    choices = Choice.objects.all()
    context = {
        'choices': choices
    }
    return render(request, 'choices/home.html', context)

class ChoiceListView(ListView):
    model = Choice
    template_name = 'choices/home.html'
    context_object_name = 'choices'
    ordering = ['-date_posted']

class ChoiceDetailView(DetailView):
    model = Choice
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preparation'] = self.object.preparation
        return context

class ChoiceCreateView(LoginRequiredMixin, CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = 'choices/choice_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user

        # picture = form.cleaned_data['picture']
        # if picture:
        #     # Upload the image to Cloudinary and get the upload result
        #     upload_result = cloudinary.uploader.upload(picture)

        #     # Print the upload result for debugging
        #     print("Upload Result:", upload_result)

        #     # Save the Cloudinary public ID to the picture field
        #     form.instance.picture = upload_result.get('public_id')

        return super().form_valid(form)


class ChoiceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # ...

    def form_valid(self, form):
        form.instance.author = self.request.user

        picture = form.cleaned_data['picture']
        if picture:
        
            upload_result = cloudinary.uploader.upload(picture)

        
            print("Upload Result:", upload_result)

        
            form.instance.picture = upload_result.get('public_id')

        return super().form_valid(form)




    
class ChoiceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Choice
    success_url = '/'

    def test_func(self):
        choice = self.get_object()
        if self.request.user == choice.author:
            return True
        return False

def about(request):
    return render(request, 'choices/about.html', {'title': 'About'})
