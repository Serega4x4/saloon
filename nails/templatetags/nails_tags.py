from django import template
import nails.views as views
from nails.models import Service, TagMaster

register = template.Library()


@register.inclusion_tag('nails/list_masters.html')
def show_masters(mas_selected=0):
    masters = Service.objects.all()
    return {'masters': masters, 'service_selected': mas_selected}


@register.inclusion_tag('nails/list_tags.html')
def show_all_tags():
    return {'tags': TagMaster.objects.all()}
