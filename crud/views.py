from .models import Student, Class, Subject
from .utils import cleanGrades
from django.shortcuts import render
from django.urls import reverse, reverse_lazy, resolve
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class BreadcrumbMixin(object):
    index = False
    verbose_name = None

    def breadcrumbUpdate(self, breadcrumb, new_value):
        for i in range(len(breadcrumb)):
            if breadcrumb[i]['url_name'] == new_value['url_name']:
                breadcrumb = breadcrumb[:i]
                break
        breadcrumb.append(new_value)
        return breadcrumb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        new_value = {
            'url_name' : resolve(self.request.path).url_name,
            'verbose_name' : self.verbose_name,
        }

        if kwargs.get('object') is not None:
            obj = kwargs['object']
        else:
            obj = context.get('object')

        if obj is not None:
            new_value['url'] = obj.get_absolute_url()
        else:
            new_value['url'] = reverse(new_value['url_name'])

        if self.index:
            self.request.session['breadcrumb'] = [new_value,]
        else:
            self.request.session['breadcrumb'] = self.breadcrumbUpdate(self.request.session['breadcrumb'], new_value)
        return context

class Index(BreadcrumbMixin, TemplateView):
    template_name = 'crud/index.html'
    index = True
    verbose_name = _('Index')

class StudentList(BreadcrumbMixin, ListView):
    template_name = 'crud/student_list.html'
    model = Student
    verbose_name = _("Students")

class StudentDetail(BreadcrumbMixin, DetailView):
    template_name = 'crud/student_detail.html'
    slug_field = 'registry'
    slug_url_kwarg = 'pk'
    verbose_name = _('View student')

    def get_queryset(self):
        return Student.objects.prefetch_related('grades').order_by('grades__order')

class StudentRegister(BreadcrumbMixin, CreateView):
    model = Student
    fields = '__all__'
    verbose_name = _('Register new student')

class StudentUpdate(BreadcrumbMixin, UpdateView):
    model = Student
    fields = '__all__'
    verbose_name = _('Update student')

class StudentDelete(BreadcrumbMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')
    verbose_name = _('Delete student')

class ClassList(BreadcrumbMixin, ListView):
    template_name = 'crud/class_list.html'
    model = Class
    queryset = Class.objects.all()
    verbose_name = _('Classes')

class ClassDetail(BreadcrumbMixin, DetailView):
    template_name = 'crud/class_detail.html'
    model = Class
    verbose_name = _('View class')

    def get_queryset(self):
        return Class.objects.prefetch_related('subjects', 'students')

class ClassRegister(BreadcrumbMixin, CreateView):
    model = Class
    fields = '__all__'
    verbose_name = _('Register new class')

class ClassUpdate(BreadcrumbMixin, UpdateView):
    model = Class
    fields = '__all__'
    verbose_name = _('Update class')

class ClassDelete(BreadcrumbMixin, DeleteView):
    model = Class
    success_url = reverse_lazy('class_list')
    verbose_name = _('Delete class')

    def get_queryset(self):
        return Class.objects.prefetch_related('subjects')

class SubjectList(BreadcrumbMixin, ListView):
    template_name = 'crud/subject_list.html'
    model = Subject
    verbose_name = _('Subjects')

class SubjectDetail(BreadcrumbMixin, DetailView):
    template_name = 'crud/subject_detail.html'
    model = Subject
    verbose_name = _('View subject')

class SubjectRegister(BreadcrumbMixin, CreateView):
    model = Subject
    fields = '__all__'
    verbose_name = _('Register new subject')

class SubjectUpdate(BreadcrumbMixin, UpdateView):
    model = Subject
    fields = '__all__'
    verbose_name = _('Update subject')

class SubjectDelete(BreadcrumbMixin, DeleteView):
    model = Subject
    success_url = reverse_lazy('subject_list')
    verbose_name = _('Delete subject')

def settings(request):
    return render(request, 'settings.html', {})
