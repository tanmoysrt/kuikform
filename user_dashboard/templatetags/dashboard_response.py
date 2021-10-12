from django import template
from django.core.validators import URLValidator

register = template.Library()


def link_builder(data):
    validate = URLValidator()
    try:
        validate(data)
        return f'''
        <a class="font-weight-bold badge badge-sm bg-gradient-dark mx-3" style="cursor: pointer"  href='{data}' target='_blank' >
          <i class="far fa-file fa-lg"></i>&nbsp;&nbsp;View File
        </a>
        '''
    except:
        return data


@register.filter
def get_value(data, target):
    if target in data:
        return link_builder(data[target])
    return "-"


@register.filter
def list_to_text_csv(data):
    result = ""
    for i in range(len(data)):
        result += data[i]
        if i != (len(data) - 1):
            result += ","
    return result
