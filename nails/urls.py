from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('photo/<slug:slug_id>/', views.photo, name='photo'),
    path('contacts/', views.contacts, name='contacts')
]