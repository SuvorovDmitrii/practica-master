from django import template
from ..models import *

register = template.Library()

@register.simple_tag(name='usluga')
def get_uslugi():
    return Uslugi.objects.all.filter(cat__exact = 'Кузовные работы')