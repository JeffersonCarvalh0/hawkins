from django.shortcuts import render
from django.utils import translation
import datetime

# Create your views here.

def index(request):
    context = {}
    template = 'index.html'
    context['today'] = datetime.date.today()

    context['cur_lang'] = request.LANGUAGE_CODE
    if request.LANGUAGE_CODE == 'en':
        context['lang'] = 'pt-br'
    elif request.LANGUAGE_CODE == 'pt-br':
        context['lang'] = 'en'

    return render(request, template, context)
