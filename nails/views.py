from django.http import HttpResponse
from django.shortcuts import render


menu = {
    "main": "Главная",
    "about": "О нас",
    "photo": "Наши работы",
    "contacts": "Контакты"
}


def main(request):
    return HttpResponse("<h1>Главная страница приложения НОГТИ</h1>")


def about(request):
    return HttpResponse("<h1>О нас</h1>")


def photo(request, slug_id):
    return HttpResponse(f"<h1>Наши работы</h1><p> Мастер: {slug_id}</p>")


def contacts(request):
    return HttpResponse("<h1>Наши контакты</h1>")

