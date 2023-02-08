from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='format_date')
def format_date(value: datetime) -> str:
    return value.strftime('%d.%m.%Y')
