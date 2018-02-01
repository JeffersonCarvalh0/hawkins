from ..utils import partial_average, total_average
from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context = True)
def back(context):
    session = context['request'].session
    prev_url = session['breadcrumb'][-2]['url']
    return prev_url

@register.simple_tag
def partial_avg(queryset):
    return partial_average(queryset)

@register.simple_tag
def total_avg(queryset):
    return total_average(queryset)

@register.filter
def subject(grades, subject):
    return grades.filter(subject=subject)

@register.filter
def addcss(field, css):
    return field.as_widget(attrs={"class":css})

@register.filter
def verbose_name(model, field):
    return model._meta.get_field(field).verbose_name
