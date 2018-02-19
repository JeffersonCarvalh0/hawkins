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

class MyModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class CreateClassFromExistingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        school_class = kwargs.pop('school_class', None)
        super().__init__(*args, **kwargs)

        self.fields['regular_grades_num'] = forms.IntegerField(initial=school_class.regular_grades_num)
        self.fields['retake_grades_num'] = forms.IntegerField(initial=school_class.retake_grades_num)
        self.fields['avg'] = forms.FloatField(initial=school_class.avg)

        self.fields['students'] = forms.ModelMultipleChoiceField(
            widget = forms.CheckboxSelectMultiple(),
            queryset = school_class.students.all(),
            required = False
        )

        self.fields['subjects'] = MyModelMultipleChoiceField(
            widget = forms.CheckboxSelectMultiple(),
            queryset = school_class.subjects.all(),
            required = False
        )

    class Meta:
        model = SchoolClass
        fields = '__all__'
