from datetime import date
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _, get_language
from .utils import documentPath, getLanguageChoices

# Create your models here.

class Settings(models.Model):
    '''
        Application's settings
    '''
    default_avg = models.FloatField(_('Default average'), default=7.00)
    default_grades_num = models.SmallIntegerField(_('Default number of regular grades'), default=3)
    default_retake_num = models.SmallIntegerField(_('Default number of retake grades'), default=1)
    lang = models.CharField(_('Language'), max_length=25, choices=getLanguageChoices(), null=True, default=get_language)

def get_default_grades_num():
    settings = Settings.objects.get_or_create(pk=0)[0]
    return settings.default_grades_num

def get_default_retake_num():
    settings = Settings.objects.get_or_create(pk=0)[0]
    return settings.default_retake_num

def get_default_avg():
    settings = Settings.objects.get_or_create(pk=0)[0]
    return settings.default_avg

class Student(models.Model):
    '''
        A Student in the school.
    '''
    name = models.CharField(_('Full name'), max_length=255)
    phone = models.CharField(_('Telephone number'), max_length=11)
    registry = models.SlugField(_('Registry'), max_length=30, unique=True, primary_key=True)
    birth = models.DateField(_('Birth date'), null=True)
    document = models.FileField(_('ID Document'), upload_to=documentPath)

    class Meta:
        verbose_name = _('Student')
        ordering = ('name',)

    def __str__(self):
        return '%s, %s' %(self.name, self.registry)

    def get_absolute_url(self):
        return reverse('student_detail', args=[self.registry])

class Subject(models.Model):
    '''
        A  school's subject. Each subject is related to a class. It is also
        related to a student, in order to store its grades. I have put 4 grades,
        but it may vary depending on the school.
    '''
    name = models.CharField(_('Name'), max_length=255)
    school_class = models.ForeignKey('SchoolClass', on_delete=models.CASCADE, verbose_name=_('Class'), related_name='subjects')

    class Meta:
        # Translators: School's subject
        verbose_name = _('Subject')

    def __str__(self):
        return '%s, %s' %(self.name, self.school_class)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        for student in self.school_class.students.all():
            i = 0
            for i in range(self.school_class.regular_grades_num):
                Grade.objects.create(order=i, student=student, subject=self)

            for i in range(i + 1, self.school_class.retake_grades_num + i + 1):
                Grade.objects.create(order=i, retake=True, student=student, subject=self)


class Grade(models.Model):
    '''
        A Student's grade of some subject.
    '''
    value = models.FloatField(_('Grade'), null=True, blank=True, default=None)
    order = models.SmallIntegerField(_('Order'))
    retake = models.BooleanField(_('Retake'), default=False)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, related_name='grades')

    class Meta:
        verbose_name = _('Grade')
        ordering = ['order']

    def __str__(self):
        return '[%s], [%s], [%.2f]' %(self.student, self.subject, self.value or 0)


class SchoolClass(models.Model):
    name = models.CharField(_('Name'), max_length=5)
    year = models.SmallIntegerField(_('Year'), default=date.today().year)
    students = models.ManyToManyField('Student', verbose_name=_('Students'), related_name='classes')
    regular_grades_num = models.SmallIntegerField(_('Number of regular grades'), default=get_default_grades_num)
    retake_grades_num = models.SmallIntegerField(_('Number of retakes'), default=get_default_retake_num)
    avg = models.FloatField(_('Average to get approved'), default=get_default_avg)

    class Meta:
        # Translators: School's grade
        verbose_name = _('Class')
        ordering = ('-year',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class_detail', args=[self.id])
