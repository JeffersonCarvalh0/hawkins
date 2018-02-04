# Some utility functions

from hawkins.settings import LANGUAGES

def documentPath(instance, filename):
    '''
        Function used to save student's documents in a path with his or her
        registry.
    '''
    return '%s/%s' %(instance.registry, filename)

def getLanguageChoices():
    '''
        Returns a list of tuples conatining the choices for the application's
        language, based on what is defined in the LANGUAGES tuple in settings.py
        file.
    '''
    choices_size = len(LANGUAGES)
    choices = [''] * choices_size

    for i in range(choices_size):
        choices[i] = (LANGUAGES[1], LANGUAGES[0])

    return choices

def partial_average(grade_queryset):
    '''
        Calculates the partial average from a queryset of grades.
    '''
    partial_avg = 0.00
    grade_counter = 0

    for grade in grade_queryset:
        if grade.value is not None:
            partial_avg += grade.value
            grade_couter += 1

    partial_avg /= grade_counter
    return partial_avg

def total_average(grade_queryset):
    '''
        Calculates the total average from a queryset of grades.
    '''
    total_avg = 0.00
    grade_counter = grade_queryset.count()

    for grade in grade_queryset:
        if grade.retake and grade.value is not None:
            total_avg += grade.value
        else:
            total_avg += grade.value or 0

    total_avg /= grade_counter
    return total_avg
