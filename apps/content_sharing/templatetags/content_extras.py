from django import template
import os
from django.utils import timezone
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def split(value, arg):
    """
    Splits the value by the argument and returns the last item
    """
    if not value:
        return ''
        
    items = value.split(arg)
    if len(items) > 0:
        return items[-1]
    return value

@register.filter
def endswith(value, arg):
    """
    Returns True if the value ends with the argument
    """
    if not value:
        return False
    return value.endswith(arg)

@register.filter
def time_since(value):
    now = timezone.now()
    diff = now - value

    if diff.days > 0:
        return f"{diff.days}g"
    
    hours = diff.seconds // 3600
    minutes = (diff.seconds % 3600) // 60
    
    if hours > 0:
        if minutes > 0:
            return f"{hours}s {minutes}dk"
        return f"{hours}s"
    
    if minutes > 0:
        return f"{minutes}dk"
    
    return "şimdi" 