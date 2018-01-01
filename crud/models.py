from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Student(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    id_document = models.CharField(_('ID Document'), max_length=30)
    registry = models.CharField(_('Registry'), max_length=30)
    age = models.SmallIntegerField(_('Age'))

    class Meta:
        verbose_name = _('Student')

    def __str__(self):
        return '%s, %s' %(self.name, self.registry)

    def get_absolute_url(self):
        return reverse('student')
