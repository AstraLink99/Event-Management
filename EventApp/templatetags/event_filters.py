from django import template

register = template.Library()

@register.filter
def calculate_progress(completed, total):
    try:
        return int((completed / total) * 100)
    except (ValueError, ZeroDivisionError):
        return 0