from .models import Student
from .utils import breadcrumbUpdate
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class Index(TemplateView):
    template_name = 'crud/index.html'
    name = _('index')
    verbose_name = _('Index')
    element = {'name' : name, 'verbose_name' : verbose_name}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'] = [self.element,]
        return context

class StudentList(ListView):
    template_name = 'crud/student_list.html'
    model = Student
    queryset = Student.objects.all()
    name = _('student_list')
    verbose_name = _("Students")
    element = {'name' : name, 'verbose_name' : verbose_name}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'] = breadcrumbUpdate(self.request.session['breadcrumb'], self.element)
        return context

class StudentDetail(DetailView):
    template_name = 'crud/student_detail'
    model = Student
    name = _('student_detail')
    verbose_name = _('View student')
    element = {'name' : name, 'verbose_name' : verbose_name}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'] = breadcrumbUpdate(self.request.session['breadcrumb'], self.element)
        return context

class StudentRegister(CreateView):
    template_name_suffix = '_register'
    model = Student
    fields = '__all__'
    name = _('student_register')
    verbose_name = _('Register new student')
    element = {'name' : name, 'verbose_name' : verbose_name}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'] = breadcrumbUpdate(self.request.session['breadcrumb'], self.element)
        return context

class StudentUpdate(UpdateView):
    template_name_suffix = '_register'
    model = Student
    fields = '__all__'
    name = _('student_update')
    verbose_name = _('Update student')
    element = {'name' : name, 'verbose_name' : verbose_name}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'] = breadcrumbUpdate(self.request.session['breadcrumb'], self.element)
        return context

class StudentDelete(DeleteView):
    template_name_suffix = '_delete'
    model = Student
    success_url = reverse_lazy('student_list')
    name = _('student_delete')
    verbose_name = _('Delete student')
    element = {'name' : name, 'verbose_name' : verbose_name}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.request.session['breadcrumb'] = breadcrumbUpdate(self.request.session['breadcrumb'], self.element)
        return context

def classes_list(request):
    return render(request,'classes_list.html', {})

def classes_detail(request):
    return render(request, 'classes_detail.html', {})

def classes_register(request):
    return render(request, 'classes_register.html', {})

def classes_update(request):
    return render(request, 'classes_update', {})

def classes_delete(request):
    return render(request, 'classes_delete.html', {})

def settings(request):
    return render(request, 'settings.html', {})
