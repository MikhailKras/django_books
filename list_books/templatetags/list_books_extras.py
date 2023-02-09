from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='format_date')
def format_date(value: datetime) -> str:
    if value is None:
        return 'Неизвестно'
    return value.strftime('%d.%m.%Y')
