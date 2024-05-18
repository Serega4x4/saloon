from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('about/', views.about, name='about'),
    path('our_works/', views.our_works, name='our_works'),
    path('contacts/', views.contacts, name='contacts'),
    path('login', views.login, name='login'),
    path('masters/<slug:master_slug>/', views.show_masters, name='masters'),
]
