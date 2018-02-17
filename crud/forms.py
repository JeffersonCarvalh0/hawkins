from .models import SchoolClass, Student, Grade, Subject
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

class CreateClassFromExistingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        school_class = kwargs.pop('school_class', None)
        super().__init__(*args, **kwargs)

        self.fields['students'] = forms.ModelMultipleChoiceField(
            widget = forms.CheckboxSelectMultiple(),
            queryset = school_class.students.all(),
            required = False
        )

        self.fields['subjects'] = forms.ModelMultipleChoiceField(
            widget = forms.CheckboxSelectMultiple(),
            queryset = Subject.objects.filter(school_class=school_class),
            required = False
        )

    class Meta:
        model = SchoolClass
        fields = '__all__'
