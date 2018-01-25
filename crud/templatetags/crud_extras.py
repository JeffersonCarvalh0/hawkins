from django import template
from django.urls import reverse
register = template.Library()

@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})

@register.simple_tag(takes_context = True)
def back(context):
    session = context['request'].session
    prev_url = session['breadcrumb'][-2]['name']

    if context.get('object'):
        return reverse(prev_url, args=[context.get('object')])
    return reverse(prev_url)
