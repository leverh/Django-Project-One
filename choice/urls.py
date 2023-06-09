from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='choice-home'),
    path('about/', views.about, name='choice-about'),
]
