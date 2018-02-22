from .models import SchoolClass, SchoolClassStudent, Student, Grade, Subject
from django import forms

class ClassAddStudentForm(forms.ModelForm):
    number = forms.IntegerField(required=False)

    def __init__(self, *args, **kwargs):
        student_instance = kwargs.pop('student_instance')
        super().__init__(*args, **kwargs)

        self.fields['student'] = forms.ModelChoiceField(
            label = str(student_instance),
            widget = forms.CheckboxInput(),
            queryset = Student.objects.filter(pk=student_instance.pk),
            required = False
        )

    class Meta:
        model = SchoolClassStudent
        fields = ('student', 'number')

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
