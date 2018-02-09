from ..utils import partial_average, total_average
from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag(takes_context = True)
def back(context):
    '''
        Returns the URL to the previous page using the breadcrumb.
    '''
    session = context['request'].session
    prev_url = session['breadcrumb'][-2]['url']
    return prev_url

@register.simple_tag
def partial_avg(queryset):
    '''
        Returns a partial average from a queryset
    '''
    return partial_average(queryset)

@register.simple_tag
def total_avg(queryset):
    '''
        Returns the total average from a queryset
    '''
    return total_average(queryset)

@register.filter
def student(grades, student):
    '''
        For a given queryset of grades and a student, returns only the grades
        of the specified student
    '''
    return grades.filter(student=student)

@register.filter
def addcss(field, css):
    '''
        Adds a css class into a django rendered html tag
    '''
    return field.as_widget(attrs={"class":css})

@register.filter
def verbose_name(model, field):
    '''
        Returns the verbose name from a model field
    '''
    return model._meta.get_field(field).verbose_name

@register.filter
def times(number):
    '''
        Range funtionality for the template
    '''
    return range(1, int(number) + 1)
