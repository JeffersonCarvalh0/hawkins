from .models import Class, Student
from django import forms

class ClassAddStudentForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        queryset = Student.objects.all(),
        required = False
    )
    
    class Meta:
        model = Class
        fields = ('students',)
