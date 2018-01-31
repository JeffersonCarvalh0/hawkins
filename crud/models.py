from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .utils import documentPath, getLanguageChoices

# Create your models here.

class Settings(models.Model):
    '''
        Application's settings
    '''
    avg = models.FloatField(_('Average'))
    lang = models.CharField(_('Language'), max_length=25, choices=getLanguageChoices())

class Student(models.Model):
    '''
        A Student in the school.
    '''
    name = models.CharField(_('Full name'), max_length=255)
    phone = models.CharField(_('Telephone number'), max_length=11)
    registry = models.SlugField(_('Registry'), max_length=30, unique=True, primary_key=True)
    birth = models.DateField(_('Birth date'), null=True)
    current_class = models.ForeignKey('Class', on_delete=models.PROTECT, null=True, verbose_name=_('Class'))
    document = models.FileField(_('ID Document'), upload_to=documentPath)

    class Meta:
        verbose_name = _('Student')

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
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name=_('Class'))

    class Meta:
        # Translators: School's subject
        verbose_name = _('Subject')

    def __str__(self):
        return '%s, %s, %s' %(self.student, self.name, self.school_class)

    def get_absolute_url(self):
        return reverse('subject_detail', args=[self.id])

class Grade(models.Model):
    '''
        A Student's grade of some subject.
    '''
    grade = models.FloatField(_('Grade'))
    order = models.SmallIntegerField(_('Order'))
    retake = models.BooleanField(_('Retake'), default=False)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)
    school_class = models.ForeignKey('Class', on_delete=models.PROTECT)

    class Meta:
        verbose_name = _('Grade')

    def __str__(self):
        return '%s, %s, %.2f' %(self.subject.student, self.subject.name, self.grade)

class Class(models.Model):
    name = models.CharField(_('Name'), max_length=5)

    class Meta:
        # Translators: School's grade
        verbose_name = _('Class')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class_detail', args=[self.id])
