from django import template

register = template.Library()

# from https://stackoverflow.com/a/33060000
@register.filter(name='addclass')
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})