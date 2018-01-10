from .models import Student
from django.shortcuts import render
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import TemplateView

# Create your views here.

class Index(TemplateView):
    template_name = 'index.html'
    name = _('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'] = [self.name,]
        return context

class Students(TemplateView):
    template_name = 'students.html'
    name = _('students')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'].append(self.name)
        return context

def students_register(request):
    return render(request, 'students_create.html', {})

def students_detail(request):
    return render(request, 'students_read.html', {})

def students_update(request):
    return render(request, 'students_update.html', {})

def students_delete(request):
    return render(request, 'students_delete.html', {})

def classes(request):
    return render(request, 'classes.html', {})

def settings(request):
    return render(request, 'settings.html', {})
