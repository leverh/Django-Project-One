from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='choices-home'),
    path('', views.home, name='choices-home'),
    path('about/', views.about, name='choices-about'),
]
