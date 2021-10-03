from django import template
import json

register = template.Library()


@register.filter
def get_value(data, target):
    if target in data:
        return data[target]
    return "-"
