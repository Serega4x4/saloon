from django import template
import nails.views as views
from nails.models import Service

register = template.Library()


@register.inclusion_tag('nails/list_masters.html')
def show_masters(mas_selected=0):
    masters = Service.objects.all()
    return {'masters': masters, 'service_selected': mas_selected}
