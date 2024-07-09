# yourapp/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter
def is_image(file_url):
    return file_url.lower().endswith(('.jpg', '.jpeg', '.png'))
