from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
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
    {'id': 1, 'title': 'Быкова Юлия', 'description': 'Быкова Юлия - жена Гриши', 'is_published': True},
    {'id': 1, 'title': 'Казакова Ольга', 'description': 'Казакова Ольга - жена Миши', 'is_published': True},
    {'id': 1, 'title': 'Краковска Агата', 'description': 'Краковска Агата - моя женая', 'is_published': True},
]

master_db = [
    {'id': 1, 'name': 'Ногти'},
    {'id': 2, 'name': 'Ресницы'},
    {'id': 3, 'name': 'Брови'},
    {'id': 4, 'name': 'Макияж'},
]


def main(request):
    master = Master.objects.filter(is_published=1)
    data = {
        'title': 'Главная',
        'menu': menu,
        'master': master,
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

def show_masters(request, mas_slug):
    master = get_object_or_404(Master, slug=mas_slug)
    data = {
        'title': master.first_name,
        'menu': menu,
        'master': master,
        'mas_selected': 1,
    }
    return render(request, 'nails/masters.html', data)


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