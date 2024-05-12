from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import TemplateView
from django.template.loader import render_to_string

from nails.models import Master


menu = [
    {'title': 'Главная', 'url_name': 'main'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Наши работы', 'url_name': 'our_works'},
    {'title': 'Связь с нами', 'url_name': 'contacts'},
    {'title': 'Войти', 'url_name': 'login'},
]


data_db = [
    {'id': 1, 'title': 'Быкова Юлия', 'description': '<h1>Быкова Юлия - жена Гриши</h1>', 'is_published': True},
    {'id': 1, 'title': 'Казакова Ольга', 'description': '<h1>Казакова Ольга - жена Миши/h1>', 'is_published': True},
    {'id': 1, 'title': 'Краковска Агата', 'description': '<h1>Краковска Агата - моя женая</h1>', 'is_published': True},
]

master_db = [
    {'id': 1, 'name': 'Ногти'},
    {'id': 2, 'name': 'Ресницы'},
    {'id': 3, 'name': 'Брови'},
    {'id': 4, 'name': 'Макияж'},
]


def main(request):
    data = {
        'title': 'Главная',
        'menu': menu,
        'main': data_db,
        'mas_selected': 0,
    }
    return render(request, 'nails/main.html', data)


# class Main(TemplateView):
#     template_name = 'main.html'
#     context_object_name = 'main'
#     title_page = 'У Юли'
#     cat_selected = 0
#
#     def get_queryset(self):
#         return Master.objects.all()

def show_masters(request, mas_id):
    data = {
        'title': 'Наши мастера',
        'menu': menu,
        'main': data_db,
        'mas_selected': mas_id,
    }
    return render(request, 'nails/main.html', data)


def about(request):
    data = {
        'title': 'О нас',
        'main': data_db,
        'menu': menu
    }
    return render(request, 'nails/about.html', context=data)


def our_works(request):
    data = {
        'title': 'Наши работы',
        'main': data_db,
        'menu': menu
    }
    return render(request, 'nails/our_works.html', context=data)


def contacts(request):
    data = {
        'title': 'Связь с нами',
        'main': data_db,
        'menu': menu
    }
    return render(request, 'nails/contacts.html', context=data)


def login(request):
    data = {
        'title': 'Войти',
        'main': data_db,
        'menu': menu
    }
    return render(request, 'nails/login.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Сраница не найдена</h1>")