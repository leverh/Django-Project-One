from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.ChoiceListView.as_view(), name='choices-home'),
    path('choice/<int:pk>/', views.ChoiceDetailView.as_view(), name='choices-detail'),
    path('choice/create/', views.ChoiceCreateView.as_view(), name='choices-create'),
    path('', views.home, name='choices-home'),
    path('about/', views.about, name='choices-about'),
]
