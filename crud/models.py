from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Student(models.Model):
    '''
        A Student in the school.
    '''
    name = models.CharField(_('Name'), max_length=255)
    registry = models.CharField(_('Registry'), max_length=30)
    birth = models.DateField(_('Birth Date'), null=True)
    school_class = models.ForeignKey('Class', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = _('Student')

    def __str__(self):
        return '%s, %s' %(self.name, self.registry)

    def get_absolute_url(self):
        return reverse('student', args=[str(self.id)])

class Document(models.Model):
    '''
        A Student's document.
    '''
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    document = models.FileField(_('Document'), upload_to=student.registry)

class Subject(models.Model):
    '''
        A  school's subject. Each subject is related to a class. It is also
        related to a student, in order to store its grades. I have put 4 grades,
        but it may vary depending on the school.
    '''
    name = models.CharField(_('Name'), max_length=255)
    grade1 = models.FloatField(_('Grade 1'), null=True)
    grade2 = models.FloatField(_('Grade 2'), null=True)
    grade3 = models.FloatField(_('Grade 3'), null=True)
    grade4 = models.FloatField(_('Grade 4'), null=True)
    rec = models.FloatField(_('Recuperation'), null=True)
    partial_avg = models.FloatField(_('Partial average'), default=0)
    total_avg = models.FloatField(_('Total average'), default=0)
    approved = models.BooleanField(_('Approved'), default=False)
    school_class = models.ForeignKey('Class', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        # Translators: School's subject
        verbose_name = _('Subject')

    def __str__(self):
        return '%s, %s, %s' %(self.student, self.name, self.school_class)

    def calcPartialAvg(self):
        pass

class Class(models.Model):
    name = models.CharField(_('Name'), max_length=5)

    class Meta:
        # Translators: School's grade
        verbose_name = _('Class')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('class', args=[str(self.id)])
