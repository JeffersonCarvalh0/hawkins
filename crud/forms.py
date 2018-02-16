from .models import SchoolClass, Student, Grade
from django import forms

class ClassAddStudentForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(
        widget = forms.CheckboxSelectMultiple(),
        queryset = Student.objects.all(),
        required = False
    )

    class Meta:
        model = SchoolClass
        fields = ('students',)
        localized_fields = ('students',)

class ClassRegisterFromExisting(forms.ModelForm):
    class Meta:
        model = SchoolClass
        exclude = ('students',)
