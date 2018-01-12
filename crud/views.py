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

def students_list(request):
    return render(request, 'students_list.html', {})

def students_register(request):
    return render(request, 'students_register.html', {})

def students_detail(request):
    return render(request, 'students_detail.html', {})

def students_update(request):
    return render(request, 'students_update.html', {})

def students_delete(request):
    return render(request, 'students_delete.html', {})

def classes_list(request):
    return render(request,'classes_list.html', {})

def classes_register(request):
    return render(request, 'classes_register.html', {})

def classes_detail(request):
    return render(request, 'classes_detail.html', {})

def classes_update(request):
    return render(request, 'classes_update.html', {})

def classes_delete(request):
    return render(request, 'classes_delete.html', {})

def settings(request):
    return render(request, 'settings.html', {})
