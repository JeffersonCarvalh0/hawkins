from .models import SchoolClass, Grade, Student
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

@receiver(m2m_changed, sender=SchoolClass.students.through, dispatch_uid='students_add')
def students_add(sender, **kwargs):
    if kwargs.get('action') == 'post_add':
        instance = kwargs.get('instance')
        for student in kwargs.get('pk_set'):
            student_instance = Student.objects.get(pk=student)
            for subject in instance.subjects.all():
                if not student_instance.grades.filter(subject=subject).exists():
                    i = 0
                    for i in range(instance.regular_grades_num):
                        Grade.objects.create(order=i, student=student_instance, subject=subject)
                    for i in range(i + 1, instance.retake_grades_num + i + 1):
                        Grade.objects.create(order=i, retake=True, student=student_instance, subject=subject)
