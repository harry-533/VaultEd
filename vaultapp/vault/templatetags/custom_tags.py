from django import template
from vault.models import *

register = template.Library()

@register.simple_tag
def get_modules():
    return Module.objects.all()