from django import template
register = template.Library()

@register.filter
def index(list, position):
    return list[position]