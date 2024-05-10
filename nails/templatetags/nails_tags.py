from django import template
import nails.views as views


register = template.Library()


@register.simple_tag(name='getmasters')
def get_masters():
    return views.master_db


@register.inclusion_tag('nails/list_masters.html')
def show_masters(mas_selected=0):
    masters = views.master_db
    return {'masters': masters, 'mas_selected': mas_selected}
