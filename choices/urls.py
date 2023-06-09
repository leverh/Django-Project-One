from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.ChoiceListView.as_view(), name='choices-home'),
    path('choice/<int:pk>/', views.ChoiceDetailView.as_view(), name='choices-detail'),
    path('choice/create/', views.ChoiceCreateView.as_view(), name='choices-create'),
    path('choice/<int:pk>/update', views.ChoiceUpdateView.as_view(), name='choices-update'),
    path('choice/<int:pk>/delete', views.ChoiceDeleteView.as_view(), name='choices-delete'),
    path('', views.home, name='choices-home'),
    path('about/', views.about, name='choices-about'),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='user-login'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
