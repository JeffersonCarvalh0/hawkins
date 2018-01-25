from .models import Student
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class BreadcrumbMixin(object):
    index = False
    name = None
    verbose_name = None

    def breadcrumbUpdate(self, breadcrumb, new_value):
        for i in range(len(breadcrumb)):
            if breadcrumb[i]['name'] == new_value['name']:
                breadcrumb = breadcrumb[:i + 1]
                return breadcrumb
        breadcrumb.append(new_value)
        return breadcrumb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_value = {'name' : self.name, 'verbose_name' : self.verbose_name}
        if self.index:
            self.request.session['breadcrumb'] = [new_value,]
        else:
            self.request.session['breadcrumb'] = self.breadcrumbUpdate(self.request.session['breadcrumb'], new_value)
        return context

class Index(BreadcrumbMixin, TemplateView):
    template_name = 'crud/index.html'
    index = True
    name = 'index'
    verbose_name = _('Index')

class StudentList(BreadcrumbMixin, ListView):
    template_name = 'crud/student_list.html'
    model = Student
    queryset = Student.objects.all()
    name = 'student_list'
    verbose_name = _("Students")

class StudentDetail(BreadcrumbMixin, DetailView):
    template_name = 'crud/student_detail'
    model = Student
    name = 'student_detail'
    verbose_name = _('View student')

class StudentRegister(BreadcrumbMixin, CreateView):
    template_name_suffix = '_register'
    model = Student
    fields = '__all__'
    name = 'student_register'
    verbose_name = _('Register new student')

class StudentUpdate(BreadcrumbMixin, UpdateView):
    template_name_suffix = '_register'
    model = Student
    fields = '__all__'
    name = 'student_update'
    verbose_name = _('Update student')

class StudentDelete(BreadcrumbMixin, DeleteView):
    template_name_suffix = '_delete'
    model = Student
    success_url = reverse_lazy('student_list')
    name = 'student_delete'
    verbose_name = _('Delete student')

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
