from django import template

register = template.Library()


@register.filter
def get_value(your_dict, key):
    return your_dict[key]
