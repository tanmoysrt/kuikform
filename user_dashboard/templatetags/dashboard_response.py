from django import template
import json

register = template.Library()


@register.filter
def get_value(data, target):
    if target in data:
        return data[target]
    return "-"

@register.filter
def list_to_text_csv(data):
    result = ""
    for i in range(len(data)):
        result += data[i]
        if i!=(len(data)-1):
            result += ","
    return result