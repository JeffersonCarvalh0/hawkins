from .forms import ClassAddStudentForm
from .models import Student, Class, Subject
from django.forms import modelform_factory, inlineformset_factory
from django.shortcuts import render
from django.urls import reverse, reverse_lazy, resolve
from django.utils.translation import ugettext as _
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

# Create your views here.

class BreadcrumbMixin(object):
    index = False
    verbose_name = None
    args_names = ['pk']

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

        args_list = []
        for arg in self.args_names:
            args_list.append(self.kwargs.get(arg))

        if self.kwargs.get('pk'):
            new_value['url'] = reverse(new_value['url_name'], args=args_list)
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
        return Student.objects.prefetch_related('classes__subjects__grades').filter(pk=self.kwargs.get('pk'))

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
    verbose_name = _('Classes')

class ClassDetail(BreadcrumbMixin, DetailView):
    template_name = 'crud/class_detail.html'
    model = Class
    verbose_name = _('View class')

    def get_queryset(self):
        return Class.objects.prefetch_related('students', 'subjects__grades__students').filter(pk=self.kwargs.get('pk'))

class ClassRegister(BreadcrumbMixin, CreateView):
    model = Class
    form_class = modelform_factory(Class, exclude=('students',))
    verbose_name = _('Register new class')

class ClassUpdate(BreadcrumbMixin, UpdateView):
    model = Class
    form_class = modelform_factory(Class, exclude=('students',))
    verbose_name = _('Update class')

class ClassDelete(BreadcrumbMixin, DeleteView):
    model = Class
    success_url = reverse_lazy('class_list')
    verbose_name = _('Delete class')

    def get_queryset(self):
        return Class.objects.prefetch_related('subjects')

class ClassAddStudent(BreadcrumbMixin, UpdateView):
    model = Class
    template_name = 'crud/class_add_student.html'
    form_class = ClassAddStudentForm
    verbose_name = _('Add students to class')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['defaults'] = [student for student in self.object.students.all().values_list('registry', flat=True)]
        return context

class ClassRemoveStudent(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        school_class = Class.objects.get(pk=kwargs.get('class'))
        student = Student.objects.get(pk=kwargs.get('student'))
        school_class.students.remove(student)
        return reverse('class_detail', args=[kwargs.get('class')])


class SubjectList(BreadcrumbMixin, ListView):
    template_name = 'crud/subject_list.html'
    model = Subject
    verbose_name = _('Subjects')

class SubjectRegister(BreadcrumbMixin, CreateView):
    model = Subject
    verbose_name = _('Register new subject')

    def get_form_class(self):
        return modelform_factory(Subject, fields=('name',))

    def form_valid(self, form):
        form.instance.school_class_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('class_detail', args=[self.kwargs.get('pk')])

class SubjectDelete(BreadcrumbMixin, DeleteView):
    model = Subject
    verbose_name = _('Delete subject')
    args_names = ['class', 'pk']

    def get_success_url(self):
        return reverse('class_detail', args=[self.kwargs.get('class')])

def settings(request):
    return render(request, 'settings.html', {})
