from django.template import Library

register = Library()

@register.filter(name='placeholder')
def placeholder(value, token):
    value.field.widget.attrs['placeholder'] = token
    return value
