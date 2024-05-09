from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import render_to_string

from nails.models import Master

menu = {"главная", "О нас", "Наши работы", "Связь с нами"}


def main(request):
    data = {
        'title': 'Главная',
        'menu': menu
    }
    return render(request, 'nails/main.html', context=data)


# class Main(TemplateView):
#     template_name = 'main.html'
#     context_object_name = 'main'
#     title_page = 'У Юли'
#     cat_selected = 0
#
#     def get_queryset(self):
#         return Master.objects.all()


def about(request):
    data = {
        'title': 'О нас',
        'menu': menu
    }
    return render(request, 'nails/about.html', context=data)


def our_works(request):
    data = {
        'title': 'Наши работы',
        'menu': menu
    }
    return render(request, 'nails/our_works.html', context=data)


def contacts(request):
    data = {
        'title': 'Связь с нами',
        'menu': menu
    }
    return render(request, 'nails/contacts.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сраница не найдена</h1>")