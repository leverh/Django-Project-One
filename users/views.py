from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from .forms import ProfilePictureForm
from django.contrib.auth.decorators import login_required
import cloudinary.uploader
import cloudinary.api

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = forms.UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! Please log-in')
            return redirect('user-login')  # Updated redirect statement
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            # Save the form to update the profile picture
            form.save()
            return redirect('profile')  # Redirect to the profile page after successful upload
    else:
        form = ProfilePictureForm(instance=user)
    return render(request, 'users/profile.html', {'form': form, 'user': user})


