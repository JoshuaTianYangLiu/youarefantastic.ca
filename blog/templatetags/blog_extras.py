from django import template
from operator import itemgetter
register = template.Library()

@register.filter
def getattribute(value, arg):
    print("REEEEEEEEEEEE",value,arg)
    return [getattr(val, arg) for val in value]
    