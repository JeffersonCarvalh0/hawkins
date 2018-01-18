from django import modelform_factory
from .models import Student

StudentForm = modelform_factory(Student, fields='__all__')
