from .forms import ClassAddStudentForm
from .models import Student, SchoolClass, Subject, Grade, Settings as hawkins_settings
from .utils import total_average
from django.forms import modelform_factory, modelformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy, resolve
from django.utils import translation
from django.utils.translation import ugettext as _
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView, ContextMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_lang = hawkins_settings.objects.get_or_create(pk=0)[0].lang
        translation.activate(user_lang)
        self.request.session[translation.LANGUAGE_SESSION_KEY] = user_lang
        return context

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

class EditGrades(BreadcrumbMixin, ContextMixin, View):
    template_name = 'crud/grades_form.html'
    args_names = ['pk', 'class']
    GradesFormset = modelformset_factory(Grade, fields=('value',), extra=0)
    verbose_name = _('Edit grades')

    def get_subjects(self, **kwargs):
        school_class = SchoolClass.objects.get(pk=kwargs.get('class'))
        subjects = Subject.objects.filter(school_class=school_class)
        return subjects

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        subjects = self.get_subjects(**kwargs)
        student = Student.objects.get(registry=kwargs.get('pk'))
        context['subjects'] = subjects

        formsets = {}
        for subject in subjects:
            subject_grades = Grade.objects.filter(subject=subject, student=student)
            formsets[subject.id] = self.GradesFormset(queryset=subject_grades, prefix=subject.id)

        context['formsets'] = formsets
        context['student'] = student
        context['class'] = SchoolClass.objects.get(pk=kwargs.get('class'))
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        subjects = self.get_subjects(**kwargs)

        for subject in subjects:
            formset = self.GradesFormset(request.POST, prefix=subject.id)
            if formset.is_valid():
                formset.save()
                return HttpResponseRedirect(reverse('student_detail', args=[kwargs.get('pk')]))


class ClassList(BreadcrumbMixin, ListView):
    template_name = 'crud/schoolclass_list.html'
    model = SchoolClass
    verbose_name = _('Classes')

class ClassDetail(BreadcrumbMixin, DetailView):
    template_name = 'crud/schoolclass_detail.html'
    model = SchoolClass
    verbose_name = _('View class')

    def get_queryset(self):
        return SchoolClass.objects.prefetch_related('students', 'subjects__grades').filter(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = kwargs.get('object')

        subjects = Subject.objects.filter(school_class=obj)
        students = Student.objects.filter(classes=obj)

        students_info = []
        subjects_num = subjects.count()

        for student in students:
            overall = 0
            averages_list = []
            for subject in subjects:
                subject_grades = Grade.objects.filter(student=student, subject=subject)
                subject_average = total_average(subject_grades)
                averages_list.append('%.2f' %(subject_average))
                overall += subject_average
            overall /= subjects.count()
            approved = overall >= obj.avg

            students_info.append({
                'name' : student.name,
                'url' : reverse('student_detail', args=[student.registry]),
                'averages_list' : averages_list,
                'overall' : '%.2f' %(overall),
                'approved' : approved,
            })

        context['students_info'] = students_info
        return context

class ClassRegister(BreadcrumbMixin, CreateView):
    model = SchoolClass
    form_class = modelform_factory(SchoolClass, exclude=('students',))
    verbose_name = _('Register new class')

class ClassUpdate(BreadcrumbMixin, UpdateView):
    model = SchoolClass
    form_class = modelform_factory(SchoolClass, exclude=('students',))
    verbose_name = _('Update class')

class ClassDelete(BreadcrumbMixin, DeleteView):
    model = SchoolClass
    success_url = reverse_lazy('class_list')
    verbose_name = _('Delete class')

    def get_queryset(self):
        return SchoolClass.objects.prefetch_related('subjects')

class ClassAddStudent(BreadcrumbMixin, UpdateView):
    model = SchoolClass
    template_name = 'crud/class_add_student.html'
    form_class = ClassAddStudentForm
    verbose_name = _('Add students to class')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['defaults'] = [student for student in self.object.students.all().values_list('registry', flat=True)]
        return context

class ClassRemoveStudent(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        school_class = SchoolClass.objects.get(pk=kwargs.get('class'))
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

class Settings(BreadcrumbMixin, UpdateView):
    model = hawkins_settings
    fields = '__all__'
    verbose_name = _('Settings')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user_lang = form.cleaned_data['lang']
        print(user_lang)
        translation.activate(user_lang)
        self.request.session[translation.LANGUAGE_SESSION_KEY] = user_lang
        return super().form_valid(form)
